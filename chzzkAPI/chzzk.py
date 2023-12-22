from .helper import CHZZK_API_BASE_URL, get_live_status_url, get_live_detail_url
from .type import *
import requests
import json

class Chzzk(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __is_valid_user_id(self) -> bool:
        if len(self.user_id) == 32:
            return True
        return False
    
    def _get_live_status(self) -> None:
        assert self.__is_valid_user_id()
        live_status_response = requests.get(get_live_status_url(self.user_id))
        self.live_status: dict = json.loads(live_status_response.text)
        
    def is_streamer_live(self) -> bool:
        self._get_live_status()
        if self.live_status['code'] == Status.OK.value and self.live_status['content'] is not None:
            return True
        return False
    
    def _get_live_detail(self) -> None:
        assert self.__is_valid_user_id()
        live_detail_response = requests.get(get_live_detail_url(self.user_id))
        self.live_detail: dict = json.loads(live_detail_response.text)

    def get_live_thumbnail(self):
        self._get_live_detail()
        return self.live_detail['content']['liveImageUrl'].replace('{type}', '720')
    
    def get_live_title(self):
        self._get_live_detail()
        return self.live_detail['content']['liveTitle']
    
    def get_live_link(self):
        return 'https://chzzk.naver.com/live/' + self.user_id
    

    
 
