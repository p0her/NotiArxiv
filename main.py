from notification.notification import ArxiVNotification
from notification.send_notification import SendNotification
from peewee import SqliteDatabase, Model, CharField
from cafeAPI.cafe import Cafe
from twitchAPI.twitch import Twitch
from afreecaAPI.afreeca import Afreeca
from chzzkAPI.chzzk import Chzzk
import asyncio
import hashlib
import aiofiles
db = SqliteDatabase('arxiv_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    webhook_url = CharField()

async def main():
    enc = hashlib.md5()
    chzzk = Chzzk()
    afreeca = Afreeca()
    twitch = Twitch()
    cafe = Cafe()
    noti = ArxiVNotification(chzzk, cafe, afreeca, twitch)
    while True:
        tasks = []
        twitch_noti_message = noti.get_twitch_noti_message()
        cafe_noti_message = noti.get_cafe_noti_message()
        afreeca_noti_message = noti.get_afreeca_noti_message()
        chzzk_noti_message = noti.get_chzzk_noti_message()
        for user in User.select():
            is_new_twitch_log = True
            is_new_cafe_log = True
            is_new_chzzk_log = True
            is_new_afreeca_log = True
            webhook_url = user.webhook_url
            tasks.append(asyncio.create_task(SendNotification(webhook_url).run(twitch_noti_message, chzzk_noti_message, afreeca_noti_message, cafe_noti_message, is_new_twitch_log, is_new_chzzk_log, is_new_afreeca_log, is_new_cafe_log)))
        
        await asyncio.gather(*tasks)
        await asyncio.sleep(10)

if __name__ == '__main__':
    asyncio.run(main())