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
import psycopg2

import os

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
MEMBER_COUNT = os.getenv('MEMBER_COUNT')
HOST = os.getenv('HOST')
DBNAME = os.getenv('DBNAME')
USER, PASSWORD = os.getenv('USER'), os.getenv('PASSWORD')
PORT = os.getenv('PORT')

conn = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD, port=PORT)
options = [
            discord.SelectOption(label='한결', default=True),
            discord.SelectOption(label='여르미', default=True),
            discord.SelectOption(label='비몽', default=True),
            discord.SelectOption(label='우사미', default=True),
            discord.SelectOption(label='에뇨', default=True),
            discord.SelectOption(label='샤르망', default=True),
            discord.SelectOption(label='고단씨', default=True),
        ]

class MemberConfig(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=120)
        self.member_checked = [False for i in range(int(MEMBER_COUNT))]
        self.member_idx = {'한결': 0, '여르미': 1, '비몽': 2, '우사미': 3, '에뇨': 4, '샤르망': 5, '고단씨': 6}
    @discord.ui.select(min_values=1, options=options, max_values=int(MEMBER_COUNT), row=2)
    async def select_option_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        for value in interaction.data['values']:
            self.member_checked[self.member_idx[value]] = True 
        await interaction.response.send_message('')

    @discord.ui.button(label='✅ 설정하기', style=discord.ButtonStyle.primary, row=1)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f'{interaction.data}')

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