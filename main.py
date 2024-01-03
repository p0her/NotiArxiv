from notification.notification import ArxiVNotification
from notification.send_notification import SendNotification
from peewee import SqliteDatabase, Model, CharField
from cafeAPI.cafe import Cafe
from twitchAPI.twitch import Twitch
from afreecaAPI.afreeca import Afreeca
from chzzkAPI.chzzk import Chzzk
from pymongo import MongoClient
import asyncio
import hashlib

async def main():
    my_client = MongoClient(host='localhost', port=27017)
    NotiArxivDB = my_client['NotiArxiv']
    webhooks = NotiArxivDB['webhooks']
    list = webhooks.find()
    for x in list:
        print(x)
    chzzk = Chzzk()
    afreeca = Afreeca()
    twitch = Twitch()
    cafe = Cafe()
    noti = ArxiVNotification(chzzk, cafe, afreeca, twitch)
    while True:
        twitch_md5 = hashlib.md5()
        cafe_md5 = hashlib.md5()
        afreeca_md5 = hashlib.md5()
        chzzk_md5 = hashlib.md5()
        tasks = []
        is_twitch_logging = False
        is_cafe_logging = False
        is_afreeca_logging = False
        is_chzzk_logging = False
        twitch_noti_message = noti.get_twitch_noti_message()
        cafe_noti_message = noti.get_cafe_noti_message()
        afreeca_noti_message = noti.get_afreeca_noti_message()
        chzzk_noti_message = noti.get_chzzk_noti_message()
        twitch_file = open('./twitch_log.txt', 'r+')
        cafe_file = open('./cafe_log.txt', 'r+')
        afreeca_file = open('./afreeca_log.txt', 'r+')
        chzzk_file = open('./chzzk_log.txt', 'r+')
        twitch_log, cafe_log, afreeca_log, chzzk_log = twitch_file.readlines(), cafe_file.readlines(), afreeca_file.readlines(), chzzk_file.readlines()
        if len(twitch_log) != 0:
            twitch_log = twitch_log[-1].strip()
        if len(cafe_log) != 0:
            cafe_log = cafe_log[-1].strip()
        if len(afreeca_log) != 0:
            afreeca_log = afreeca_log[-1].strip()
        if len(chzzk_log) != 0:
            chzzk_log = chzzk_log[-1].strip()
        twitch_md5.update(str(twitch_noti_message).encode())
        cafe_md5.update(str(cafe_noti_message).encode())
        afreeca_md5.update(str(afreeca_noti_message).encode())
        chzzk_md5.update(str(chzzk_noti_message).encode())
        if twitch_md5.hexdigest() != twitch_log:
            is_twitch_logging = True
            twitch_file.write(twitch_md5.hexdigest()+'\n')
        if cafe_md5.hexdigest() != cafe_log:
            is_cafe_logging = True
            cafe_file.write(cafe_md5.hexdigest()+'\n')
        if afreeca_md5.hexdigest() != afreeca_log:
            is_afreeca_logging = True
            afreeca_file.write(afreeca_md5.hexdigest()+'\n')
        if chzzk_md5.hexdigest() != chzzk_log:
            is_chzzk_logging = True
            chzzk_file.write(chzzk_md5.hexdigest()+'\n')
        list = webhooks.find()
        for user in list:
            tasks.append(asyncio.create_task(SendNotification(user['webhook']).run(twitch_noti_message, chzzk_noti_message, afreeca_noti_message, cafe_noti_message, is_twitch_logging, is_chzzk_logging, is_afreeca_logging, is_cafe_logging)))
        await asyncio.gather(*tasks)
        twitch_file.close()
        cafe_file.close()
        afreeca_file.close()
        chzzk_file.close()
        await asyncio.sleep(10)


if __name__ == '__main__':
    asyncio.run(main())