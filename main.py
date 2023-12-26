from notification.notification import ArxiVNotification
from peewee import SqliteDatabase, Model, CharField
from cafeAPI.cafe import Cafe
import asyncio

db = SqliteDatabase('arxiv_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    webhook_url = CharField()

async def main():
    cafe = Cafe()
    tasks = []
    db.connect()
    for i,user in enumerate(User.select()):
        noti = ArxiVNotification(user.webhook_url, cafe)
        tasks.append(asyncio.create_task(noti.cafe_run()))
    for task in tasks:
        await task
    cafe.driver_close()
    db.close()
    
if __name__ == '__main__':
    while True:
        asyncio.run(main())

