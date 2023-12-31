import hashlib
import asyncio
from chzzkAPI.chzzk import Chzzk
from afreecaAPI.afreeca import Afreeca
from cafeAPI.cafe import Cafe
from twitchAPI.twitch import Twitch
from type import ChzzkUserID, UserName, ProfileUrl, ColorID, AfreecaUserID, TwitchUserID
from discordBot.app import DiscordBot

REQUEST_TIME = 10

class ArxiVNotification(object):
    def __init__(self, webhook_url: str):
        self.chzzk = Chzzk()
        self.bot = DiscordBot(webhook_url)
        self.cafe = Cafe()
        self.afreeca = Afreeca()
        self.twitch = Twitch()
        self.webhook_url = webhook_url
        self.color = ColorID
        self.dictName = {'한결':'HANGYEOL', '여르미':'YEORUMI', '비몽':'BEEMONG', '우사미':'U32', '에뇨':'ENYO', '샤르망':'CHARMANTE'}
        self.twitch_id = [x.value for x in TwitchUserID]
        self.afreeca_id = [x.value for x in AfreecaUserID]
        self.chzzk_id = [x.value for x in ChzzkUserID]

    def generate_noti_message(self, name, avatar_url, title, description, stream_url, color, image_url):
        webhook_message = {}
        webhook_message['username'] = name
        webhook_message['avatar_url'] = avatar_url
        webhook_message['embeds'] = [
            {
                'title': f'{title}',
                'description': f'{description}',
                'url': f'{stream_url}',
                'color': color,
                'image': {
                    'url': f'{image_url}'
                }
            }
        ]
        return webhook_message
    
    def generate_cafe_noti_message(self, name, avatar_url, title, announcement_url, color, author, thumbnail_url = None):
        webhook_message = {}
        webhook_message['username'] = name
        webhook_message['avatar_url'] = avatar_url
        webhook_message['embeds'] = [
            {
                'author': {
                    'name': f'{author}'
                },
                'title': f'{title}',
                'url': f'{announcement_url}',
                'color': color,
            }
        ]
        if thumbnail_url is not None:
            webhook_message['embeds'][0]['image'] = {
                'url': f'{thumbnail_url}'
            }

        return webhook_message
    
    def get_cafe_noti_message(self):
        announcement_list = self.cafe.get_announcement()
        announcement = announcement_list[0]
        writer, title, announcement_url = announcement[0], announcement[1], announcement[2]
        avatar_url = getattr(ProfileUrl, self.dictName[writer]).value
        color = getattr(ColorID, self.dictName[writer]).value
        urls_split = announcement_url.split('&')
        article_id = 0
        for param in urls_split:
            if 'articleid' in param:
                article_id = int(param.split('=')[1])
                break
        thumbnail_url = self.cafe.get_img_src('godanssity', article_id)
        author = '📺 방송 공지'
        ret = self.generate_cafe_noti_message(writer, avatar_url, title, announcement_url, color, author, thumbnail_url)
        return ret


    def get_chzzk_noti_message(self):
        is_live = [0 for i in range(len(self.chzzk_id))]
        titles = ['' for i in range(len(self.chzzk_id))]
        viewer_counts = [0 for i in range(len(self.chzzk_id))]
        broad_urls = ['' for i in range(len(self.chzzk_id))]
        thumbnail_urls = ['' for i in range(len(self.chzzk_id))]
        ret = [False for i in range(len(self.chzzk_id))]
        idx = [i for i in range(len(self.chzzk_id))]

        for i, user_id in enumerate(self.chzzk_id):
            if self.chzzk.is_streamer_live(user_id):
                is_live[i] = True
                
        for i, user_id in enumerate(self.chzzk_id):
            if not is_live[i]: continue
            titles[i] = self.chzzk.get_live_title(user_id)
            viewer_counts[i] = self.chzzk.get_live_user_count(user_id)
            broad_urls[i] = self.chzzk.get_live_link(user_id)
            thumbnail_urls[i] = self.chzzk.get_live_thumbnail(user_id)

        for (i, user_id, name, color, avatar_url) in zip(idx, self.chzzk_id, UserName, self.color, ProfileUrl):
            if not is_live[i]: continue
            ret[i] = self.generate_noti_message(name.value, avatar_url.value, f'{name.value} 뱅온', titles[i], broad_urls[i], color.value, thumbnail_urls[i])
        
        return ret

    def get_afreeca_noti_message(self):
        is_live = [0 for i in range(len(self.afreeca_id))]
        titles = ['' for i in range(len(self.afreeca_id))]
        viewer_counts = [0 for i in range(len(self.afreeca_id))]
        broad_urls = ['' for i in range(len(self.afreeca_id))]
        thumbnail_urls = ['' for i in range(len(self.afreeca_id))]
        broad_no = [0 for i in range(len(self.afreeca_id))]
        ret = [False for i in range(len(self.afreeca_id))]
        idx = [i for i in range(len(self.afreeca_id))]

        for i, user_id in enumerate(self.afreeca_id):
            if self.afreeca.is_bj_live(user_id):
                is_live[i] = True

        for i, user_id in enumerate(self.afreeca_id):
            if not is_live[i]: continue
            titles[i] = self.afreeca.get_broad_title(user_id)
            viewer_counts[i] = self.afreeca.get_broad_current_viewer(user_id)
            broad_no[i] = self.afreeca.get_broad_no(user_id)
            broad_urls[i] = self.afreeca.get_broad_url(user_id, broad_no[i])
            thumbnail_urls[i] = self.afreeca.get_thumbnail_url(user_id)

        for (i, user_id, name, color, avatar_url) in zip(idx, self.afreeca_id, UserName, self.color, ProfileUrl):
            if not is_live[i]: continue
            ret[i] = self.generate_noti_message(name.value, avatar_url.value, f'{name.value} 뱅온', titles[i], broad_urls[i], color.value, thumbnail_urls[i])
        
        return ret
    
    def get_twitch_noti_message(self):
        is_live = [0 for i in range(len(self.twitch_id))]
        titles = ['' for i in range(len(self.twitch_id))]
        viewer_counts = [0 for i in range(len(self.twitch_id))]
        broad_urls = ['' for i in range(len(self.twitch_id))]
        thumbnail_urls = ['' for i in range(len(self.twitch_id))]
        ret = [False for i in range(len(self.twitch_id))]
        idx = [i for i in range(len(self.twitch_id))]

        for i, user_id in enumerate(self.twitch_id):
            if self.twitch.is_stream(user_id):
                is_live[i] = True

        for i, user_id in enumerate(self.twitch_id):
            if not is_live[i]: continue
            stream_information = self.twitch.get_stream_information(user_id)[0]
            titles[i] = self.twitch.get_title(stream_information)
            viewer_counts[i] = self.twitch.get_viewer_count(stream_information)
            broad_urls[i] = self.twitch.get_broad_url(user_id)
            thumbnail_urls[i] = self.twitch.get_thumbnail_url(stream_information)

        for (i, user_id, name, color, avatar_url) in zip(idx, self.twitch_id, UserName, self.color, ProfileUrl):
            if not is_live[i]: continue
            ret[i] = self.generate_noti_message(name.value, avatar_url.value, f'{name.value} 뱅온', titles[i], broad_urls[i], color.value, thumbnail_urls[i])

        return ret
    
    def twitch_noti_run(self):
        twitch_noti_message = self.get_twitch_noti_message()
        for x in twitch_noti_message:
            if x is not False:
                self.bot.send_twitch_live_on_message(x)

    def chzzk_noti_run(self):
        chzzk_noti_message = self.get_chzzk_noti_message()
        for x in chzzk_noti_message:
            if x is not False:
                self.bot.send_chzzk_live_on_message(x)

    def afreeca_noti_run(self):
        afreeca_noti_message = self.get_afreeca_noti_message()
        for x in afreeca_noti_message:
            if x is not False:
                self.bot.send_afreeca_live_on_message(x)
            
    def cafe_noti_run(self):
        cafe_noti_message = self.get_cafe_noti_message()
        self.bot.send_cafe_announcement_message(cafe_noti_message)

    def run(self):
        self.cafe_noti_run()
        self.chzzk_noti_run()
        self.afreeca_noti_run()
        self.twitch_noti_run()