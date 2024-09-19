from pytubefix import YouTube
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


def baixar_video(url):
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path='data')
    
def baixar_audio(url):
    yt = YouTube(url)
    ys = yt.streams.get_audio_only()
    ys.download(mp3=True, filename=f'{yt.title}audio', output_path='data')
    
def transcrever_audio(audio_path):
    client = openai.Client()
    audio = open('audio_path', 'rb')
    transcricao = client.audio.transcription.create(
        model='whisper',
        file=audio,
        response_format='srt' #srt gera uma saida em formato de legenda, com tempo de inicio e fim
        )
    return transcricao