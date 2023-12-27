from enum import Enum

class UserID(Enum):
    ID_HANGYEOL = '9f16e0bfbb7a9ee1fdabce002047b82b'
    ID_YEORUMI = '726482d31891e0808d6289e2497791fc'
    ID_BEEMONG = '39c3d49d1e1becc865f42ee251329766'
    ID_U32 = '60ddec4bc4beab3fbf4f7c2d1aa7d70d'
    #ID_ENYO = '' # todo : chzzk URL update
    #ID_CHARMANTE = '' # todo : chzzk URL update

class UserName(Enum):
    HANGYEOL = '한결'
    YEORUMI = '여르미'
    BEEMONG = '비몽'
    U32 = '우사미'
    ENYO = '에뇨'
    CHARMANTE = '샤르망'

class ProfileUrl(Enum):
    HANGYEOL = 'https://pbs.twimg.com/profile_images/1703254263630385152/Sa2O5xl-_400x400.jpg'
    YEORUMI = 'https://pbs.twimg.com/profile_images/1707165905728520192/-3CqemlL_400x400.jpg'
    BEEMONG = 'https://pbs.twimg.com/profile_images/1736782646834020352/tguD2xmk_400x400.jpg'
    U32 = 'https://pbs.twimg.com/profile_images/1721162598081789952/3-KTR_a2_400x400.jpg'
    ENYO = 'https://pbs.twimg.com/profile_images/1737478829466116096/XkByc9HR_400x400.jpg'
    CHARMANTE = 'https://pbs.twimg.com/profile_images/1727610264521187328/dx0NRpMT_400x400.jpg'

class ColorID(Enum):
    HANGYEOL = 0xfeb9c6
    YEORUMI = 0x5884ff
    BEEMONG = 0xbfd4e7
    U32 = 0xda3396
    ENYO = 0x53493e
    CHARMANTE = 0x5f4f7c

class AfreecaUserID(Enum):
    HANGYEOL = 'kaksjak0730'
    YEORUMI = 'yeorumi030'
    BEEMONG = 'beemong'

class TwitchUserID(Enum):
    HANGYEOL = 'hangyeol8008'
    YEORUMI = 'yeorumi030'
    BEEMONG = 'beemong_'
    U32 = 'u32__'
    ENYO = 'enyo_sekai'
    CHARMANTE = '0owo0__'
