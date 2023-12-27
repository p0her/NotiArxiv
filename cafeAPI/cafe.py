from selenium import webdriver
from bs4 import BeautifulSoup
from requests.utils import requote_uri
from .helper import get_stream_announcement_url

class Cafe:
    def __init__(self):
        self.announcement_url = get_stream_announcement_url()
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(options=options) 

    def driver_close(self):
        self.driver.quit()
        
    def get_announcement(self):
        self.driver.get(self.announcement_url)
        self.driver.switch_to.frame('cafe_main')
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        soup = soup.find_all(class_='article-board m-tcol-c')[1]
        data = soup.find_all(class_='td_article')[0]
        article_title = data.find(class_='article')
        link = article_title.get('href')
        article_title = article_title.get_text().strip()
        article_title = article_title.split(']')
        writer = article_title[0].replace('[', '')
        title = article_title[1].split('\n')[-1].strip()
        link = link.replace('&', '%26').replace('?', '%3F').replace('=', '%3D')
        link = 'https://cafe.naver.com/godanssity?iframe_url_utf8=' + link
        return [writer, title, link]


            