from .helper import *
import requests

class Twitch:
    def __init__(self):
        self.headers = {
            'Client-id': '3u2bps8wk79a8e16h9ln1zxt9k41ob',
            'Authorization' : 'Bearer ' + 'eoasqa7ais7tzuhznkvgd9599sil4y'
        }

    def get_user(self, user_id) -> dict:
        res = requests.get(get_user_url(user_id), headers=self.headers)
        return res.json()
    
    def get_channel_information(self, user_id) -> dict:
        res = requests.get(get_channel_infromation_url(user_id), headers=self.headers)
        return res.json()
    
    def get_stream(self, user_id) -> dict:
        res = requests.get(get_stream_url(user_id), headers=self.headers)
        return res.json()

    def is_stream(self, user_id) -> bool:
        res = self.get_stream(user_id)
        if not res['data']:
            return False
        return True

    def get_stream_information(self, user_id) -> list:
        res = self.get_stream(user_id)
        return res['data']

    def get_title(self, stream_information: dict) -> str:
        return stream_information['title']
    
    def get_viewer_count(self, stream_information: dict) -> int:
        return stream_information['viewer_count']
    
    def get_broad_url(self, user_id: str) -> str:
        return 'https://www.twitch.tv/' + user_id
    
    def get_thumbnail_url(self, stream_information: dict) -> str:
        return stream_information['thumbnail_url'].replace('{width}', '440').replace('{height}', '248')
           