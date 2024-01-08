from .type import Status
import requests
import aiohttp

class DiscordBot(object):
    def __init__(self, webhook_url: str) -> None:
        self.webhook_url = webhook_url
    
    async def send_live_information_message(self, streamer_name: str, notice_link: str):
        '''
        parse stream schedule from naver cafe. 
        '''
        return None
        
    async def send_cafe_announcement_message(self, webhook_message: dict) -> requests.Response:
        async with aiohttp.ClientSession() as session:
            await session.post(self.webhook_url, json=webhook_message)

    async def send_afreeca_live_on_message(self, webhook_message: dict) -> requests.Response:
        async with aiohttp.ClientSession() as session:
            await session.post(self.webhook_url, json=webhook_message)