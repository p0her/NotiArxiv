import time
from chzzkAPI.chzzk import Chzzk
from type import UserID, UserName, ProfileUrl
from discordBot.app import DiscordBot

REQUEST_TIME = 10
class ArxiVNotification(object):
    def __init__(self, webhook_url: str):
        self.members = [Chzzk(x.value) for x in UserID] 
        self.bot = DiscordBot(webhook_url)

    def run(self):
        while True:
            for member, streamer_name, profile_url in zip(self.members, UserName, ProfileUrl):
                if member.is_streamer_live():
                    self.bot.send_stream_on_message(member.user_id, streamer_name.value, profile_url.value)
            time.sleep(REQUEST_TIME)

