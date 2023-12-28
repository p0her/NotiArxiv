TWITCH_API_USER_URL: str = 'https://api.twitch.tv/helix/users?login='
TWITCH_API_CHANNEL_INFORMATION_URL: str = 'https://api.twitch.tv/helix/channels?broadcaster_id='
TWITCH_API_STREAMS_URL: str = 'https://api.twitch.tv/helix/streams?user_login='

def get_user_url(id: str):
    return TWITCH_API_USER_URL + id

def get_channel_infromation_url(id: str):
    return TWITCH_API_CHANNEL_INFORMATION_URL + id

def get_stream_url(id: str):
    return TWITCH_API_STREAMS_URL + id

