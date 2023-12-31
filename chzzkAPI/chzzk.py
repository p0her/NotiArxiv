from .helper import CHZZK_API_BASE_URL, get_live_status_url, get_live_detail_url
from .type import *
import requests

class Chzzk(object):
    def __init__(self):
        print('Chzzk')
        
    def _get_live_status(self, user_id):
        live_status_response = requests.get(get_live_status_url(user_id))
        return live_status_response.json()
        
    def is_streamer_live(self, user_id) -> bool:
        live_status = self._get_live_status(user_id)
        if live_status['code'] == Status.OK.value and live_status['content'] is not None and live_status['content']['status'] == 'OPEN':
            return True
        return False
    
    def _get_live_detail(self, user_id):
        live_detail_response = requests.get(get_live_detail_url(user_id))
        live_detail  = live_detail_response.json()
        return live_detail

    def get_live_thumbnail(self, user_id):
        live_detail = self._get_live_detail(user_id)
        if live_detail['content'] is not None:
            return live_detail['content']['liveImageUrl'].replace('{type}', '720')
    
    def get_live_title(self, user_id):
        live_detail = self._get_live_detail(user_id)
        if live_detail['content'] is not None:
            return live_detail['content']['liveTitle']
        else:
            return None
        
    def get_live_link(self, user_id):
        return 'https://chzzk.naver.com/live/' + user_id
    
    def get_live_id(self, user_id):
        live_detail = self._get_live_detail(user_id)
        if live_detail['content'] is not None:
            return live_detail['content']['liveId']
        else:
            return None
        
    def get_live_user_count(self, user_id):
        live_detail = self._get_live_detail(user_id)
        if live_detail['content'] is not None:
            return live_detail['content']['concurrentUserCount']
        else:
            return None