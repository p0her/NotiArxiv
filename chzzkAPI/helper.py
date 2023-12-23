CHZZK_API_BASE_URL: str = 'https://api.chzzk.naver.com'
CHZZK_LIVE_STATUS_URL: str = '/polling/v1/channels/'
CHZZK_LIVE_DETAIL_URL: str = '/service/v1/channels/'

def get_live_status_url(user_id : str):
    return CHZZK_API_BASE_URL + CHZZK_LIVE_STATUS_URL + user_id + '/live-status'

def get_live_detail_url(user_id : str):
    return CHZZK_API_BASE_URL + CHZZK_LIVE_DETAIL_URL + user_id + '/live-detail'