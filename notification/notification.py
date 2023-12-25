import time
import hashlib
import asyncio
from chzzkAPI.chzzk import Chzzk
from cafeAPI.cafe import Cafe
from type import UserID, UserName, ProfileUrl
from discordBot.app import DiscordBot

REQUEST_TIME = 10

class ArxiVNotification(object):
    def __init__(self, webhook_url: str):
        self.members = [Chzzk(x.value) for x in UserID] 
        self.bot = DiscordBot(webhook_url)
        self.cafe = Cafe()
        self.webhook_url = webhook_url

    async def discord_run(self):
        f = open('./live_log.txt', 'r+') 
        enc = hashlib.md5()
        log_lines = f.readlines()
        for member, streamer_name, profile_url in zip(self.members, UserName, ProfileUrl):
            if member.is_streamer_live() and member.get_live_id() is not None:
                enc.update(str(member.get_live_id()).encode())
                member_live_id = enc.hexdigest()
                is_logging = True
                for log_line in log_lines:
                    t = log_line.split(' ')
                    if self.webhook_url == t[0] and t[1].strip() == member_live_id:
                        is_logging = False
                        break
                if is_logging:
                    self.bot.send_stream_on_message(member.user_id, streamer_name.value, profile_url.value)
                    f.write(self.webhook_url + ' ' + member_live_id + '\n')
        f.close()
        await asyncio.sleep(REQUEST_TIME)

    def cafe_run(self):
        f = open('./cafe_log.txt', 'r+')
        self.cafe.get_announcement()
        f.close()