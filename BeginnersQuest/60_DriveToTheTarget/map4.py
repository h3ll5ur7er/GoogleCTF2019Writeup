from collections import OrderedDict
from bs4 import BeautifulSoup
from requests import get
from re import match
from math import sin, cos, asin, acos, degrees, radians
from time import sleep
from pprint import pprint
from sys import stdout
from threading import Thread, Event
from functools import wraps

import folium

url = "https://drivetothetarget.web.ctfcompetition.com/"
token = "gAAAAABdGjMnAFqy-oVh0KNzw3fyptOWW5yq4Pvu-O_NrVXeHQS5GYneFdrS1lXiYJTPINFDXfwZqzdWjpq5aqgNXOhlSI27gfyhotFjiG150QjXn_ydNimisDnQIFulCucwOwm0P6S4"

lat_min = -90
lat_max = 90

lon_min = -180
lon_max = 180

def set_interval(interval):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            stopped = Event()

            def loop():
                while not stopped.wait(interval):
                    function(*args, **kwargs)
            
            t = Thread(target=loop)
            t.daemon = True
            t.start()
            return stopped
        return wrapper
    return decorator

class Parser:
    def parse(self, response):
        soup = BeautifulSoup(response, "html.parser")
        lat = float(soup.find("input", attrs={"name":"lat"})["value"])
        lon = float(soup.find("input", attrs={"name":"lon"})["value"])
        token = soup.find("input", attrs={"name":"token"})["value"]
        msg = soup.find_all("p")[-1].get_text()
        return msg, lat, lon, token


class Driver:
    def __init__(self, url):
        self.url = url
        self.parser = Parser()
        self.dx = 0
        self.dy = 0
        self.speed = 0.0001
        _, self.next_lat, self.next_lon, self.next_token = self.parser.parse(get(self.url).text)
        
        self.map = folium.Map(location=[self.next_lat, self.next_lon],
                              zoom_start=10)

        folium.CircleMarker(
            location=[self.next_lat, self.next_lon],
            radius=5,
            popup='Origin',
            color="#888888",
            fill=True,
            fill_color="#888888"
        ).add_to(self.map)
        self.prev_lat = self.next_lat
        self.prev_lon = self.next_lon
        self.prev_token = self.next_token

        self.request  = lambda lat, lon, token: self.parser.parse(get(self.url, {"lat":lat, "lon":lon, "token":token}).text)
        self.handlers = {
            "stopped" : self.not_moving,
            "good" : self.good_direction,
            "bad" : self.bad_direction,
            "tooFast" : self.too_fast,
            "tooFar" : self.too_far,
            "unhandled" : self.unhandled,
        }

        self.patterns = {
            r"If you want to meet your friends, you should move": "stopped",
            r"(?:You went )(\d*m)(?: at a speed of )(\d*km\/h)(?:\. You are getting )(away|closer)": "valid",
            r"Woa, were about to move at (\d*km\/h), this is too fast!": "tooFast",
            r"You tried to travel (\d*m), which too far at once from your current position": "tooFar",
        }

        self.search_good_direction(10)

        self.stop_mapping = self.save_map()

    def get_state(self, msg, log=True):
        for pattern, state in self.patterns.items():
            m = match(pattern, msg)
            if m is not None:
                if state == "valid":
                    distance, speed, result = m.groups()
                    _speed = float(speed[:-4])
                    if log:
                        if speed != 0 and _speed < 20:
                            self.speed *= 2
                        stdout.write(distance + " @ " + speed + " : ")
                        stdout.flush()
                    return "good" if result == "closer" else "bad"
                return state
        else:
            print("unknown state: ", msg)
            return "unhandled"


    def step(self):
        msg, new_lat, new_lon, new_token = self.request(self.next_lat, self.next_lon, self.next_token)
        self.next_lat, self.next_lon, self.next_token = self.handlers[self.get_state(msg)](msg, new_lat, new_lon, new_token)

    @set_interval(10)
    def save_map(self):
        self.map.save("map.html")

    def search_good_direction(self, step_size=5):
        results = {}
        sleep(2)
        for angle in range(0, 360, step_size):
            dx = cos(radians(angle))
            dy = sin(radians(angle))*2
            _lat = self.next_lat + dx*self.speed
            _lon = self.next_lon + dy*self.speed
            folium.CircleMarker(
                location=[_lat, _lon],
                radius=1,
                popup='Scanning',
                color="#888888",
                fill=True,
                fill_color="#888888"
            ).add_to(self.map)
            msg, new_lat, new_lon, new_token = self.request(_lat, _lon, self.next_token)
            state = self.get_state(msg, False)
            results[angle] = [state, new_lat, new_lon, new_token]
        passing_zero = results[list(results.keys())[0]][0] == "good" and results[list(results.keys())[-1]][0]
        avg = 0 
        good_results = {a: v for a,v in results.items() if v[0] == "good"}
        for angle, _ in good_results.items():
            if passing_zero:
                angle += 180 + angle
                angle %= 360
            else:
                avg += angle
        print("good angles: ", list(good_results.keys())[0], "", list(good_results.keys())[-1], " passing zero" if passing_zero else "")
        avg /= len(good_results)
        if passing_zero:
            avg += 180
            avg %= 360
        
        dx = cos(radians(avg))
        dy = sin(radians(avg))

        _lat = self.next_lat + dx*self.speed
        _lon = self.next_lon + dy*self.speed
        folium.CircleMarker(
            location=[_lat, _lon],
            radius=2,
            popup='newTarget',
            color="#008888",
            fill=True,
            fill_color="#008888"
        ).add_to(self.map)
        self.dx = dx
        self.dy = dy
        msg, self.next_lat, self.next_lon, new_token = self.request(self.next_lat + self.dx*self.speed, self.next_lon + self.dy*self.speed, self.next_token)
        

    
    ### HANDLERS ###
    def not_moving(self, msg, new_lat, new_lon, new_token):
        print("driver is not moving")
        return self.next_lat + self.dx * self.speed, self.next_lon + self.dy * self.speed, self.next_token

    def too_fast(self, msg, new_lat, new_lon, new_token):
        print("too fast..")
        self.speed /= 3
        sleep(1)
        return new_lat + self.dx*self.speed, new_lon + self.dy*self.speed, new_token

    def too_far(self, msg, new_lat, new_lon, new_token):
        print("too far..")
        self.speed /= 3
        sleep(1)
        return new_lat, new_lon, new_token

    def good_direction(self, msg, new_lat, new_lon, new_token):
        print("go on..", self.next_lat, ", ", self.next_lon)
        folium.CircleMarker(
            location=[self.next_lat, self.next_lon],
            radius=1,
            popup='Origin',
            color="#00ffff",
            fill=True,
            fill_color="#00ffff"
        ).add_to(self.map)
        return new_lat + self.dx*self.speed, new_lon + self.dy*self.speed, new_token

    def bad_direction(self, msg, new_lat, new_lon, new_token):
        print("stop, reverse and look for new direction")
        self.search_good_direction()
        return self.next_lat, self.next_lon, self.next_token

    def unhandled(self, msg, new_lat, new_lon, new_token):
        print("> unhandled message: ", msg)
        exit(0)
        return self.next_lat, self.next_lon, self.next_token
    
    

if __name__ == "__main__":
    d = Driver(url)
    while 1:
        try:
            d.step()
        finally:
            d.stop_mapping.set()
    

#lat = 51.6498
#lon = 0.0982


