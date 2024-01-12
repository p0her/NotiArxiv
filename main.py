from notification.notification import ArxiVNotification
from notification.send_notification import SendNotification
from cafeAPI.cafe import Cafe
from afreecaAPI.afreeca import Afreeca
import discord
from discord.ext import commands
from dotenv import load_dotenv
#from youtubeAPI.youtube import Youtube
import asyncio
import os

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
MEMBER_COUNT = os.getenv('MEMBER_COUNT')
HOST = os.getenv('HOST')
DBNAME = os.getenv('DBNAME')
USER, PASSWORD = os.getenv('USER'), os.getenv('PASSWORD')
PORT = os.getenv('PORT')
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)
commands_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'commands')

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.default(),
            allowed_mentions=discord.AllowedMentions.none(),
        )
    async def setup_hook(self):
        await self.load_extension('commands.member_setting')
        await self.tree.sync()

bot = Bot()
bot.run(BOT_TOKEN)