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

async def main():
    tasks = []
    for i,user in enumerate(User.select()):
        noti = ArxiVNotification(user.webhook_url)
        tasks.append(asyncio.create_task(noti.run()))

    for task in tasks:
        await task
    
if __name__ == '__main__':
    while True:
        asyncio.run(main())