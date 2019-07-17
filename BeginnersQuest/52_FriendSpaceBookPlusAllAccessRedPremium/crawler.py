from os import system
from requests import get as http_get
from html.parser import HTMLParser
from pprint import pprint
from collections import OrderedDict
from shutil import copyfileobj

SEARCH_ROOT = "http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com"
SEARCH_DEPTH = 5

pages = {}

dbg = False

def wget(uri):
    system("wget "+uri)

class Page(HTMLParser):
    def __init__(self, uri):
        super().__init__()
        self.uri = uri
        self.links = set()
        self.data = []
        self.id = -1
        self.scan = False

    def crawl(self):
        self.response = http_get(self.uri)
        self.feed(self.response.text)
        if "CTF{" in self.response.text:
            exit(0)
        return [SEARCH_ROOT+"/"+l for l in self.links], self.response

    def handle_data(self, data):
        if self.scan:
            self.data.append(data)
            self.scan = False

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.scan = True
            for key, val in attrs:
                if key == 'href':
                    self.links.add(val)
        elif tag == "img":
            self.scan = False
            for key, val in attrs:
                if key == 'src':
                    self.id = int(val.split("-")[1].split(".")[0])
        #             wget(SEARCH_ROOT+"/"+val)
        else:
            self.scan = False



def crawl(uri):
    page = Page(uri)
    links, response = page.crawl()
    pages[uri] = page
    # print(response.text)
    # print("\n----------------------------------------------------------------------------------------------\n")
    return links

def main(*args):
    all_pages = [SEARCH_ROOT]
    idx = 0
    while idx<len(all_pages):
        if dbg:
            print("crawling ", all_pages[idx], " (",idx," of ", len(all_pages), ")...")
        response = crawl(all_pages[idx])
        for link in response:
            if link not in all_pages:
                all_pages.append(link)
        idx += 1


    pprint(all_pages)
    for page in sorted(pages, key=lambda k: p.id):
        print(page.id)
        pprint(page.data)

if __name__ == "__main__":
    from sys import argv
    main(*argv[1:])
