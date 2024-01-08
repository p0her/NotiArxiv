from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .helper import *
from ..type import YoutubeUserID, YoutubeClipUserID, YoutubeReplayUserID

class Youtube:
    def __init__(self):
        self.youtube = build('youtube', 'v3', developerKey=get_youtube_api_key())
    
    def get_cnt(self, channel_id):
        channel_response = self.youtube.channels().list(
            part='statistics',
            id=channel_id
        ).execute()
        print(channel_response)
        video_count =  int(channel_response['items'][0]['statistics']['videoCount'])
        return video_count
    
    def get_video_response(self, channel_id):
        request = self.youtube.search().list(
            part='id,snippet',
            channelId=channel_id,
            order='date',
            type='video',
            maxResults=1
        )
        response = request.execute()
        response = response['items'][0]
        video_title = response['snippet']['title']
        video_id = response['id']['videoId']

        return video_title, video_id

if __name__ == '__main__':
    youtube = Youtube()
    for user in YoutubeClipUserID:
        try:
            print(youtube.get_video_response(user.value))
        except:
            continue
    