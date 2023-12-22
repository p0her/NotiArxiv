from notification.notification import ArxiVNotification
from peewee import SqliteDatabase, Model, CharField
import asyncio

db = SqliteDatabase('arxiv_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    webhook_url = CharField()

db.connect()
db.create_tables([User])

async def main():
    tasks = []
    webhook_urls = [
        'https://discord.com/api/webhooks/1187768288571301928/sX9VavD4LGjx_m8MYRDsM5FN_oa_zUBoYxNTgw-28zKHdBlhAmVPVSZZe1T3ll7Gdfq0',
        'https://discord.com/api/webhooks/1187768399602917427/SaOwJSSj2yBLbfXyZaEqSgvA-TFDLw_b3i6Lb8chE1-K_SSwL72iPqFDG96juHZdOmSY',
        'https://discord.com/api/webhooks/1187768453357125733/AGOKPivu7h_cav0ag_TsnCr_dXEdJ1Urd3JnCe3Aij0NkZNYmGiY8ga9OGkh9ZT0jTbX',
        'https://discord.com/api/webhooks/1187768490812260404/6C0Q8Js9Za_ck_gB_oPN4y44FZ3X6_2TzvHggZTnCrzipDA2ssw6Amt8YrN67w3g8b55',
        'https://discord.com/api/webhooks/1187768535099912354/o_OiHSw90GBmueIN3FAhm0UpsVamqC12SM2a_pE72OZUMYD1EPTRlebcSrTVgJ5q7xq_',
    ]

    for webhook_url in webhook_urls:
        user, created = User.get_or_create(webhook_url = webhook_url)
    for i,user in enumerate(User.select()):
        noti = ArxiVNotification(user.webhook_url)
        tasks.append(noti.run())
    await asyncio.gather(tasks)
    print('hi')

if __name__ == '__main__':
    asyncio.run(main())