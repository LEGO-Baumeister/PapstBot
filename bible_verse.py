from bs4 import BeautifulSoup
import requests

class BibleVerse():
    def __init__(self):
        pass

    def get_verse(self):
        URL = "https://dailyverses.net/de/zufalls-bibelvers"
        page = requests.get(URL).text.encode("utf-8")
        soup = BeautifulSoup(page, 'html.parser')

        span = soup.find('span', {"class" : "v1"})
        text = span.string

        a = soup.find('a', {"class" : "vc"})
        source = a.string

        if source == None:
            return get_verse()
        else:
            as_array = [text, source]
            return as_array

