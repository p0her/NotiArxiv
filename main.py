from notification.notification import ArxiVNotification
from notification.send_notification import SendNotification
from cafeAPI.cafe import Cafe
from afreecaAPI.afreeca import Afreeca
from discord.ext import commands
from discord import ui
from dotenv import load_dotenv
#from youtubeAPI.youtube import Youtube
import asyncio
import discord

import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

class MemberConfig(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=120)

    @discord.ui.button(label='primary', style=discord.ButtonStyle.primary, row=1)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('button1')


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.tree.command(name='멤버세팅', description='원하는 멤버의 알림을 설정할 수 있습니다.')
async def slash_command(interaction:discord.Interaction):
    embed = discord.Embed(title="멤버 알림 설정", description="", color=0x32363c)
    await interaction.response.send_message(embed=embed, view=MemberConfig())

@bot.tree.command(name='방송정보', description='멤버들의 방송 정보를 보여줍니다.')
async def slash_command(interaction:discord.Interaction):
    await interaction.response.send_message('방송 정보 테스트')

'''
@bot.tree.command(name='저메추', description='뭘 말해도 어차피 지 먹고 싶은 거 먹을 텐데')

    await interaction.response.send_message(food)
'''

@bot.event
async def on_ready():
    await bot.tree.sync()

bot.run(BOT_TOKEN)