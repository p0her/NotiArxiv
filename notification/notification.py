from afreecaAPI.afreeca import Afreeca
from cafeAPI.cafe import Cafe
from type import UserName, ProfileUrl, ColorID, AfreecaUserID
import logging
REQUEST_TIME = 10

class ArxiVNotification(object):
    def __init__(self, chzzk, cafe, afreeca, twitch):
        self.chzzk = chzzk
        self.cafe = cafe
        self.afreeca = afreeca
        self.twitch = twitch
        self.color = ColorID
        self.dictName = {'한결':'HANGYEOL', '여르미':'YEORUMI', '비몽':'BEEMONG', 'u32':'U32', '에뇨':'ENYO', '샤르망':'CHARMANTE', '고단씨': 'GODANSSI'}
        self.afreeca_id = [x.value for x in AfreecaUserID]

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
            thumbnail_urls[i] = self.afreeca.get_thumbnail_url(broad_no[i])

        for (i, user_id, name, color, avatar_url) in zip(idx, self.afreeca_id, UserName, self.color, ProfileUrl):
            if not is_live[i]: continue
            ret[i] = self.generate_noti_message(name.value, avatar_url.value, f'{name.value} 뱅온', titles[i], broad_urls[i], color.value, thumbnail_urls[i])
        
        return ret
    
    def get_youtube_noti_message(self):
        None