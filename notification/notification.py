import time
import hashlib
import asyncio
from chzzkAPI.chzzk import Chzzk
from afreecaAPI.afreeca import Afreeca
from cafeAPI.cafe import Cafe
from type import UserID, UserName, ProfileUrl, ColorID, AfreecaUserID
from discordBot.app import DiscordBot

REQUEST_TIME = 10

class ArxiVNotification(object):
    def __init__(self, webhook_url: str, cafe: Cafe, afreeca: Afreeca):
        self.members = [Chzzk(x.value) for x in UserID] 
        self.bot = DiscordBot(webhook_url)
        self.cafe = cafe
        self.afreeca = [Afreeca(x.value) for x in AfreecaUserID]
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

    async def cafe_run(self):
        f = open('./cafe_log.txt', 'r+')
        dictName = {'한결':'HANGYEOL', '여르미':'YEORUMI', '비몽':'BEEMONG', '우사미':'U32', '에뇨':'ENYO', '샤르망':'CHARMANTE'}
        enc = hashlib.md5()
        log_lines = f.readlines()
        announcement = self.cafe.get_announcement()
        enc.update(str(announcement[0] + announcement[1] + announcement[2] + self.webhook_url).encode())
        x = enc.hexdigest()
        if x+'\n' not in log_lines:
            self.bot.send_cafe_announcement(getattr(ColorID, dictName.get(announcement[0])).value, '📺 방송 공지', announcement[1], announcement[2], announcement[0], getattr(ProfileUrl,dictName.get(announcement[0])).value)
            f.write(x+'\n')
        f.close()
        await asyncio.sleep(REQUEST_TIME)

    async def afreeca_run(self):
        f = open('./afreeca_log.txt', 'r+')
        enc = hashlib.md5()
        log_lines = f.readlines()
        for member, streamer_name in zip(self.afreeca, UserName):
            broad_title = member.get_broad_title()
            broad_no = member.get_broad_no()
            current_sum_viewer = member.get_broad_current_viewer()
            broad_url = member.get_broad_url()
            enc.update(str(broad_no).encode() + self.webhook_url.encode())
            x = enc.hexdigest()
            if x+'\n' not in log_lines:
                self.bot.send_afreeca_live_on_message()
                f.write(x+'\n')
            f.close()
            await asyncio.sleep(REQUEST_TIME)

    async def twitch_run(self):
        None
