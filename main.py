import schedule
import time
from notification.notification import ArxiVNotification

if __name__ == '__main__':
    webhook_url = 'https://discord.com/api/webhooks/1187385356170039418/BJ9jDELXOrYn2TO6ylxvGG5sbhCbG2rJlEJ3EtagzLXBx2WxX-UtqGRCJQHVLj7sTYJk'
    noti = ArxiVNotification(webhook_url)
    noti.run()