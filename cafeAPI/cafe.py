import re
import requests
from bs4 import BeautifulSoup
from typing import Self
from .helper import get_stream_announcement_url

class Cafe:
    def __init__(self):
        self.announcement_url = get_stream_announcement_url()
        self.announcement_res = requests.get(self.announcement_url)
        print(self.announcement_res.text)
        self.soup = BeautifulSoup(self.announcement_res.text, 'lxml')
    
    def get_announcement(self):
        print(self.soup.select('article-board m-tcol-c'))