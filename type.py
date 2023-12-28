from enum import Enum

class ChzzkUserID(Enum):
    ID_HANGYEOL = '9f16e0bfbb7a9ee1fdabce002047b82b'
    ID_YEORUMI = '726482d31891e0808d6289e2497791fc'
    ID_BEEMONG = '39c3d49d1e1becc865f42ee251329766'
    ID_U32 = '60ddec4bc4beab3fbf4f7c2d1aa7d70d'
    ID_ENYO = 'UNDEFINED_ENYO' # todo : chzzk URL update
    ID_CHARMANTE = 'UNDEFINED_CHARMANTE' # todo : chzzk URL update
    ID_GODANSSI = 'UNDEFINED_GODANSSI'
    
class UserName(Enum):
    HANGYEOL = '한결'
    YEORUMI = '여르미'
    BEEMONG = '비몽'
    U32 = '우사미'
    ENYO = '에뇨'
    CHARMANTE = '샤르망'
    GODANSSI = '고단씨'

class ProfileUrl(Enum):
    HANGYEOL = 'https://pbs.twimg.com/profile_images/1703254263630385152/Sa2O5xl-_400x400.jpg'
    YEORUMI = 'https://pbs.twimg.com/profile_images/1707165905728520192/-3CqemlL_400x400.jpg'
    BEEMONG = 'https://pbs.twimg.com/profile_images/1736782646834020352/tguD2xmk_400x400.jpg'
    U32 = 'https://pbs.twimg.com/profile_images/1721162598081789952/3-KTR_a2_400x400.jpg'
    ENYO = 'https://pbs.twimg.com/profile_images/1737478829466116096/XkByc9HR_400x400.jpg'
    CHARMANTE = 'https://pbs.twimg.com/profile_images/1727610264521187328/dx0NRpMT_400x400.jpg'
    GODANSSI = 'https://cafeptthumb-phinf.pstatic.net/MjAyMzEyMTdfNzYg/MDAxNzAyODA1ODM4NTM2.b-os7btGmD_rUo7adIZ699kV-ioKpehEpt1praoqGakg.2yoKvtt9N_jNxvdY5X0qGQlygQB3bVXJEkpd77xeVXIg.JPEG/1700378491.829309.jpeg?type=w1600'

class ColorID(Enum):
    HANGYEOL = 0xfeb9c6
    YEORUMI = 0x5884ff
    BEEMONG = 0xbfd4e7
    U32 = 0xda3396
    ENYO = 0x53493e
    CHARMANTE = 0x5f4f7c
    GODANSSI = 0x000000

class AfreecaUserID(Enum):
    HANGYEOL = 'kaksjak0730'
    YEORUMI = 'yeorumi030'
    BEEMONG = 'beemong'
    U32 = 'UNDEFINED_U32'
    ENYO = 'UNDEFINED_ENYO'
    CHARMANTE = 'UNDEFINED_CHARMANTE'
    GODANSSI = 'UNDEFINED_GODANSSI'

class TwitchUserID(Enum):
    HANGYEOL = 'hangyeol8008'
    YEORUMI = 'yeorumi030'
    BEEMONG = 'beemong_'
    U32 = 'u32__'
    ENYO = 'enyo_sekai'
    CHARMANTE = '0owo0__'
    GODANSSI = 'godan9184'