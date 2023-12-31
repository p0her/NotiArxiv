from chzzkAPI.chzzk import Chzzk
from .type import Status
import requests

class DiscordBot(object):
    def __init__(self, webhook_url: str) -> None:
        self.webhook_url = webhook_url
    
    def send_live_information_message(self, streamer_name: str, notice_link: str):
        '''
        parse stream schedule from naver cafe. 
        '''
        return None
        
    def send_cafe_announcement_message(self, webhook_message: dict) -> requests.Response:
        res = requests.post(self.webhook_url, json=webhook_message)
        return res
    
    def send_chzzk_live_on_message(self, webhook_message: dict) -> requests.Response:
        res = requests.post(self.webhook_url, json=webhook_message)
        return res
    
    def send_afreeca_live_on_message(self, webhook_message: dict) -> requests.Response:
        res = requests.post(self.webhook_url, json=webhook_message)
        return res
        
    def send_twitch_live_on_message(self, webhook_message: dict) -> requests.Response:
        res = requests.post(self.webhook_url, json=webhook_message)
        return res