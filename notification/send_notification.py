from discordBot.app import DiscordBot
import hashlib

REQUEST_TIME = 10

class SendNotification(object):
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.bot = DiscordBot(webhook_url)

    async def twitch_noti_run(self, twitch_noti_message):
        for x in twitch_noti_message:
            if x is not False:
                await self.bot.send_twitch_live_on_message(x)

    async def chzzk_noti_run(self, chzzk_noti_message):
        for x in chzzk_noti_message:
            if x is not False:
                await self.bot.send_chzzk_live_on_message(x)

    async def afreeca_noti_run(self, afreeca_noti_message):
        for x in afreeca_noti_message:
            if x is not False:
                await self.bot.send_afreeca_live_on_message(x)
            
    async def cafe_noti_run(self, cafe_noti_message):
        await self.bot.send_cafe_announcement_message(cafe_noti_message)

    async def run(self, twitch_noti_message, chzzk_noti_message, afreeca_noti_message, cafe_noti_message, is_new_twitch_log, is_new_chzzk_log, is_new_afreeca_log, is_new_cafe_log):
        if is_new_twitch_log:
            await self.twitch_noti_run(twitch_noti_message)
        if is_new_chzzk_log:
            await self.chzzk_noti_run(chzzk_noti_message)
        if is_new_afreeca_log:
            await self.afreeca_noti_run(afreeca_noti_message)
        if is_new_cafe_log:
            await self.cafe_noti_run(cafe_noti_message)