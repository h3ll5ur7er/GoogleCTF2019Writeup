
from html.parser import HTMLParser
from requests import get
from re import compile as regex
from json import dumps
from pprint import pprint
import folium
from os import system
from time import sleep, time
from http.server import BaseHTTPRequestHandler, HTTPServer
from geopy.distance import distance

url = "https://drivetothetarget.web.ctfcompetition.com/"
token = "gAAAAABdGjMnAFqy-oVh0KNzw3fyptOWW5yq4Pvu-O_NrVXeHQS5GYneFdrS1lXiYJTPINFDXfwZqzdWjpq5aqgNXOhlSI27gfyhotFjiG150QjXn_ydNimisDnQIFulCucwOwm0P6S4"
# token = "gAAAAABdHEKSkzu_E3uqkonUyc5mYcOtwFZXQlCDyP0wnzfjz-k-G94UNrJ5h2l-Efrnww_0eyUubsX0iFhUA6DNMeZSkWfEM21qLUnxcuA6cbv5s00_EtlV3WtgSOT1fcw1UXPlKlxs"

lat_min = -90
lat = 51.6498
# lat = 51.62429999999988
lat_max = 90

lon_min = -180
lon = 0.0982
# lon = -0.034399999999999556
lon_max = 180



o =  [51.6498, 0.0982]
n =  [51.6508, 0.0981]
s =  [51.6489, 0.0984]
w =  [51.6498, 0.0960]
e =  [51.6500, 0.0999]
ne = [51.6505, 0.0995]
se = [51.6497, 0.1001]
sw = [51.6492, 0.0969]
nw = [51.6505, 0.0970]



class Message:
    def __init__(self, *a, **kw):
        self.speed = "undefined"
        self.distance = "undefined"
        self.args = a
        self.kw_args = kw
    def __str__(self):
        return "Message type undefined"

class UnknownMessage(Message):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.args = a
        self.kw_args = kw
    def __str__(self):
        return "Message unknown: a:{}, kw:{}".format(self.args, self.kw_args)

class TooFarMessage(Message):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.distance = a[0]
    def __str__(self):
        return "Too far: {}".format(self.distance)

class AwayMessage(Message):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.distance = a[0]
        self.speed = a[1]
    def __str__(self):
        return "WrongDirection: distance: {}, speed:{}".format(self.distance, self.speed)

class CloserMessage(Message):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.distance = a[0]
        self.speed = a[1]
    def __str__(self):
        return "GoodDirection: distance: {}, speed:{}".format(self.distance, self.speed)

regexes = {
    "You tried to travel (\d*m)": TooFarMessage,
    "You went (\d*m) at a speed of (\d*km/h). You are getting away…":AwayMessage,
    "You went (\d*m) at a speed of (\d*km/h). You are getting closer…":CloserMessage,
}


class Page(HTMLParser):
    def __init__(self, uri, lat, lon):
            # for key, val in attrs:
            #     if key == 'src':
            #         self.id = int(val.split("-")[1].split(".")[0])
        #             wget(SEARCH_ROOT+"/"+val)
        super().__init__()
        self.uri = uri
        self.data = []
        self.value = None
        self.lat = lat
        self.lon = lon
        self.token = token
        self.scan = False
        self.last_request = 0
        self.map = folium.Map(location=[lat, lon],
                zoom_start=90)

        folium.Circle(
            location=[self.lat, self.lon],
            radius=10,
            popup='Origin',
            color="#00ffff",
            fill=True,
            fill_color="#00ffff"
        ).add_to(self.map)

    def handle_data(self, data):
        if self.scan:
            self.scan = False
            if data.startswith("Hurry up"):
                return
            for pattern, msg_type in regexes.items():
                r = regex(pattern)
                m = r.match(data)
                if m:
                    self.data.append(msg_type(*m.groups()))
                    return
            self.data.append(UnknownMessage(data))

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            self.scan = False
            self.value = None
            for key, val in attrs:
                if key == 'value':
                    if self.value is None:
                        self.value = val
                    else:
                        if self.value in ["lat", "lon"]:
                            val = float(val)
                        setattr(self, self.value, val)
                if key == 'name':
                    if self.value is None:
                        self.value = val
                    else:
                        if val in ["lat", "lon"]:
                            self.value = float(val)
                        setattr(self, val, self.value)
        elif tag == "p":
            self.scan = True
        else:
            self.scan = False

    def get(self, d_lat, d_lon):
        _lat = self.lat+d_lat
        _lon = self.lon+d_lon
        return self.get_abs(_lat, _lon)

    def get_abs(self, _lat, _lon, token = None):
        if token is None:
            token = self.token
        if _lat < lat_min:
            _lat += 2*lat_max
        if _lat > lat_max:
            _lat -= 2*lat_max

        if _lon < lon_min:
            _lon += 2*lon_max
        if _lon > lon_max:
            _lon -= 2*lon_max
        
        dist = distance([self.lat, self.lon], [_lat, _lon]).meters
        
        speed = 10000000
        while speed>48:
            sleep(1)
            t = time()
            dt = t - self.last_request
            speed = (dist / dt) * 3.6

        self.last_request = t

        self.response = get(self.uri, {"token":token, "lat":_lat, "lon":_lon})
        self.feed(self.response.text)
        if isinstance(self.data[-1], CloserMessage):
            color = "#00ff00"
        elif isinstance(self.data[-1], AwayMessage):
            color = "#ff0000"
        elif isinstance(self.data[-1], UnknownMessage):
            color = "#000000"
        elif isinstance(self.data[-1], TooFarMessage):
            color = "#ffffff"
        else:
            color = "#ffff00"


        folium.Circle(
            location=[self.lat, self.lon],
            radius=10,
            popup='Origin',
            color=color,
            fill=True,
            fill_color=color
        ).add_to(self.map)
        self.map.save("map.html")
        
        return self.data[-1]

    def __str__(self):
        return str(serialize_response(self.response))

def serialize_response(response):
    data = {}
    for entry in dir(response):
        value = getattr(response, entry)
        try:
            dumps({entry:value})
            data[entry] = value
        except:
            pass
    return data




class Agent:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def try_move(self, d_lat, d_lon):
        pass




def main(*args):

    """
    m = folium.Map(location=origin,
                zoom_start=100)
                
    folium.Circle(
        location=origin,
        radius=50,
        popup='Origin',
        color='#3186cc',
        fill=True,
        fill_color='#3186cc'
    ).add_to(m)
    m.add_child(folium.ClickForMarker())
    m.add_child(folium.LatLngPopup())
    m.save("map.html")
    system("firefox map.html")
    exit(0)"""

    p = Page(url, lat, lon)

    d_lat = 51.6493-lat
    d_lon = 0.0956-lon

    for _ in range(10000):
        m = p.get(d_lat, d_lon)
        print("{},{},{},{},{},{},{},{},".format(type(m).__name__, m.distance, m.speed, p.lat, p.lon, p.token, m.args, m.kw_args))
        if "Away" in type(m).__name__:
            exit(0)



if __name__ == "__main__":
    from sys import argv
    main(*argv[1:])
