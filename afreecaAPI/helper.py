AFREECA_API_BASE_URL = 'https://bjapi.afreecatv.com/api/'
AFREECA_LIVE_BASE_URL = 'https://play.afreecatv.com/'

def get_station_api_url(user_id: str):
    return AFREECA_API_BASE_URL + user_id + '/station'
