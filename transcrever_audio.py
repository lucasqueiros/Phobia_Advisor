import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

audio = open('audio.mp3', 'rb')

transcricao = client.audio.transcription.create(
    model='whisper',
    file=audio,
    response_format='srt' #srt gera uma saida em formato de legenda, com tempo de inicio e fim
)

print(transcricao)