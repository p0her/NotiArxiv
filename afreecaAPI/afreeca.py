from .helper import get_station_api_url, AFREECA_LIVE_BASE_URL, AFREECA_LIVE_IMAGE_URL
import requests
import json

class Afreeca:
    def __init__(self):
        print('Afreeca')
        
    def _get_live_status(self, user_id):
        live_detail_response = requests.get(get_station_api_url(user_id), headers = {'User-Agent': 'Mozilla/5.0'})
        return live_detail_response.json()

    def is_bj_live(self, user_id):
        live_detail = self._get_live_status(user_id)
    
        if 'broad' not in live_detail:
            return False
        if live_detail['broad'] == None:
            return False
        else:
            return True
        
    def _get_broad_status(self, user_id):
        live_detail = self._get_live_status(user_id)
        return live_detail['broad']
    
    def get_broad_no(self, user_id):
        return self._get_broad_status(user_id)['broad_no']

    def get_broad_title(self, user_id):
        return self._get_broad_status(user_id)['broad_title']

    def get_broad_current_viewer(self, user_id):
        return self._get_broad_status(user_id)['current_sum_viewer']
    
    def get_broad_url(self, user_id: str, broad_no: int):
        return AFREECA_LIVE_BASE_URL + user_id + '/' + str(broad_no)
    
    def get_thumbnail_url(self, broad_no: int):
        return AFREECA_LIVE_IMAGE_URL + 'm/' + str(broad_no)
    

        