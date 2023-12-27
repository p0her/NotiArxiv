from helper import get_station_api_url, AFREECA_LIVE_BASE_URL
import requests
import json
class Afreeca:
    def __init__(self, user_id):
        self.user_id: str = user_id
        self.live_detail: dict = {}

    def _get_live_status(self):
        live_detail_response = requests.get(get_station_api_url(self.user_id), headers = {'User-Agent': 'Mozilla/5.0'})
        self.live_detail: dict = json.loads(live_detail_response.text)

    def is_bj_live(self):
        self._get_live_status()
        if self.live_detail['broad'] == None:
            return False
        else:
            return True
        
    def _get_broad_status(self):
        self._get_live_status()
        return self.live_detail['broad']
    
    def get_broad_no(self):
        return self._get_broad_status()['broad_no']

    def get_broad_title(self):
        return self._get_broad_status()['broad_title']

    def get_broad_current_viewer(self):
        return self._get_broad_status()['current_sum_viewer']
    
    def get_broad_url(self, user_id: str, broad_no ; int):
        return AFREECA_LIVE_BASE_URL + user_id + '/' + str(broad_no)

        