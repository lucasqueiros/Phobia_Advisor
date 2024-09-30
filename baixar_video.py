import sys
from pytubefix import YouTube


def baixar_video(url):
    yt = YouTube(url, client='WEB_CREATOR')
    ys = yt.streams.get_highest_resolution()
    output_path = 'data'
    ys.download(output_path=output_path, filename='video.mp4')
    return f'{output_path}/video.mp4'
