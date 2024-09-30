import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


def transcrever_audio(audio_path):
    
    client = openai.Client()
    audio = open(audio_path, 'rb')
    transcricao = client.audio.transcriptions.create(
        model='whisper-1',
        file=audio,
        response_format='srt' #srt gera uma saida em formato de legenda, com tempo de inicio e fim
    )
    with open('data/transcricao.txt', 'w') as f:
        f.write(transcricao)
    return transcricao
