from notification.notification import ArxiVNotification
from notification.send_notification import SendNotification
from cafeAPI.cafe import Cafe
from afreecaAPI.afreeca import Afreeca
#from youtubeAPI.youtube import Youtube
import asyncio
import discord
from discord.ext import commands

BOT_TOKEN = 'MTE4NzM4MjcxNzQzMjc0NjIwNg.GYkjP3.6dKMfLdW04vK-0D9U2IvZCyjSOTGQwh0ODUUsA'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/',intents=intents)

@bot.tree.command(name='멤버세팅', description='원하는 멤버의 알림을 설정할 수 있습니다.')
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message('멤버 세팅 테스트')

bot.run(BOT_TOKEN)