from discordBot.app import DiscordBot
import hashlib

REQUEST_TIME = 10
BOT_URL = 'https://discord.com/api/oauth2/authorize?client_id=1187382717432746206&permissions=8&scope=bot'
BOT_TOKEN = 'MTE4NzM4MjcxNzQzMjc0NjIwNg.GHEtgy.UDNsWRwMUm_zzpiAG4rZNhm2tUX5nfcfQQFxnk'

class SendNotification(object):
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.bot = DiscordBot(webhook_url)

    async def afreeca_noti_run(self, afreeca_noti_message):
        for x in afreeca_noti_message:
            if x is not False:
                await self.bot.send_afreeca_live_on_message(x)
            
    async def cafe_noti_run(self, cafe_noti_message):
        await self.bot.send_cafe_announcement_message(cafe_noti_message)

    async def run(self, afreeca_noti_message, cafe_noti_message, is_afreeca_logging, is_cafe_logging):
        if is_afreeca_logging:
            await self.afreeca_noti_run(afreeca_noti_message)
        if is_cafe_logging:
            await self.cafe_noti_run(cafe_noti_message)