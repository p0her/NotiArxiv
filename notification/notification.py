import time
import hashlib
import asyncio
from chzzkAPI.chzzk import Chzzk
from type import UserID, UserName, ProfileUrl
from discordBot.app import DiscordBot

REQUEST_TIME = 10

class ArxiVNotification(object):
    def __init__(self, webhook_url: str):
        self.members = [Chzzk(x.value) for x in UserID] 
        self.bot = DiscordBot(webhook_url)
        self.webhook_url = webhook_url

    async def run(self):
        while True:
            f = open('./live_log.txt', 'r+') 
            enc = hashlib.md5()
            log_lines = f.readlines()
            for member, streamer_name, profile_url in zip(self.members, UserName, ProfileUrl):
                if member.is_streamer_live() and member.get_live_id() is not None:
                    enc.update(str(member.get_live_id()).encode())
                    member_live_id = enc.hexdigest()
                    if member_live_id +'\n' not in log_lines:
                        if self.webhook_url not in log_lines:
                            self.bot.send_stream_on_message(member.user_id, streamer_name.value, profile_url.value)
                            f.write(self.webhook_url + ' ' + member_live_id + '\n')
            f.close()
            await asyncio.sleep(REQUEST_TIME)