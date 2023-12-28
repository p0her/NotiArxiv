from chzzkAPI.chzzk import Chzzk
from .type import Status
import requests

class DiscordBot(object):
    def __init__(self, webhook_url: str) -> None:
        self.webhook_url = webhook_url
        
    def send_stream_on_message(self, color_id, title, link, thumbnail, streamer_name: str, streamer_profile_image_url: str) -> bool:
        webhook_message = {}
        webhook_message['username'] = '[알림] ' + streamer_name
        webhook_message['avatar_url'] = streamer_profile_image_url
        webhook_message['embeds'] = [
            {
                'color': str(color_id),
                'title': f'{title}',
                'url': f'{link}',
                'image': {
                    'url': f'{thumbnail}'
                }
            }
        ]
        res = requests.post(self.webhook_url,json=webhook_message)
        if res.status_code == Status.NO_CONTENT:
            return True
        else:
            return False
    
    def send_live_information_message(self, streamer_name: str, notice_link: str):
        '''
        parse stream schedule from naver cafe. 
        '''
        return None
    
    def send_cafe_announcement(self, color_id: int, title: str, name:str, url: str, streamer_name: str, streamer_profile_image_url: str) -> bool:
        webhook_message = {}
        webhook_message['username'] = '[알림] ' + streamer_name
        webhook_message['avatar_url'] = streamer_profile_image_url
        webhook_message['embeds'] = [
            {
                'color': str(color_id),
                'title': f'{title}',
                'author': {
                    'name': f'{name}',
                    'url': f'{url}'
                },
            }
        ]
        print(webhook_message)
        res = requests.post(self.webhook_url,json=webhook_message)
        if res.status_code == Status.OK:
            return True
        else:
            return False
        
    def send_chzzk_live_on_message(self, webhook_message: dict) -> bool:
        res = requests.post(self.webhook_url, json=webhook_message)
        print(res)
        return res
    
    def send_afreeca_live_on_message(self, webhook_message: dict) -> bool:
        res = requests.post(self.webhook_url, json=webhook_message)
        print(res)
        return res
        
    def send_twitch_live_on_message(self, webhook_message: dict) -> bool:
        res = requests.post(self.webhook_url, json=webhook_message)
        print(res)
        return res