from selenium import webdriver
from bs4 import BeautifulSoup
from .helper import get_stream_announcement_url
import requests
class Cafe:
    def __init__(self):
        print('Cafe')
        self.announcement_url = get_stream_announcement_url()
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(options=options) 
        self.driver.get(get_stream_announcement_url())
        self.driver.implicitly_wait(3)

    def driver_close(self):
        self.driver.quit()
        
    def get_article(self, cafe_id, article_id) -> dict:
        fetch_url = f'https://apis.naver.com/cafe-web/cafe-articleapi/v2.1/cafes/{cafe_id}/articles/{article_id}?useCafeId=false'
        return requests.get(fetch_url).json()['result']

    def get_content(self, cafe_id, article_id):
        article = self.get_article(cafe_id, article_id)
        return article['article']['contentHtml']
    
    def get_img_src(self, cafe_id, article_id):
        content = self.get_content(cafe_id, article_id)
        soup = BeautifulSoup(content, 'html.parser')
        img = soup.select('img')
        if not img:
            return None 
        img = img[0]
        return img.get_attribute_list('src')[0]
    
    def get_announcement(self) -> list:
        self.driver.switch_to.frame('cafe_main')
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        titles = soup.select("#main-area > div:nth-child(4) > table > tbody > tr")
        ret = []
        for title in titles:
            x = (title.select_one(' td.td_article > div.board-list > div > a'))
            url = 'https://cafe.naver.com' + x.get_attribute_list('href')[0]
            list = (x.text).split()
            writer = list[0].replace('[', '').replace(']', '')
            list = list[1:]
            title = ' '.join(list)
            ret.append([writer, title, url])
        self.driver.get(get_stream_announcement_url())
        return ret
    