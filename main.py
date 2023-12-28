from notification.notification import ArxiVNotification
from peewee import SqliteDatabase, Model, CharField
from cafeAPI.cafe import Cafe
from twitchAPI.twitch import Twitch
from afreecaAPI.afreeca import Afreeca
from chzzkAPI.chzzk import Chzzk
import asyncio

db = SqliteDatabase('arxiv_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    webhook_url = CharField()

if __name__ == '__main__':
    noti = ArxiVNotification('https://discord.com/api/webhooks/1187768399602917427/SaOwJSSj2yBLbfXyZaEqSgvA-TFDLw_b3i6Lb8chE1-K_SSwL72iPqFDG96juHZdOmSY')
    noti.run()

