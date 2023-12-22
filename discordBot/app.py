from chzzkAPI.type import Status
from chzzkAPI.chzzk import Chzzk
import requests
class DiscordBot(object):
    def __init__(self, webhook_url: str) -> None:
        self.webhook_url = webhook_url
    def send_stream_on_message(self, user_id: str, streamer_name: str, streamer_profile_image_url: str) -> bool:
        chzzk = Chzzk(user_id)
        webhook_message = {}
        webhook_message['username'] = '[알림] ' + streamer_name
        webhook_message['avatar_url'] = streamer_profile_image_url
        webhook_message['embeds'] = [
            {
                'title': f'{chzzk.get_live_title()}',
                'url': f'{chzzk.get_live_link()}',
                'image': {
                    'url': chzzk.get_live_thumbnail()
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
    
    def send_cafe_announcement(self):
        None
    
