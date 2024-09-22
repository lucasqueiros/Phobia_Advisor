import baixar_video
import extrair_audio
import transcrever_audio
import os
import json
import atexit

CACHE_FILE = '/home/lucasqueiros/CC/Phobia_Advisor/transcription_cache.txt'

# Load the cache from the file if it exists
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, 'r') as file:
        transcription_cache = json.load(file)
else:
    transcription_cache = {}

def save_cache():
    with open(CACHE_FILE, 'w') as file:
        json.dump(transcription_cache, file)

# Ensure the cache is saved when the script exits
atexit.register(save_cache)

def run_pipeline(link, fobia):
    if link in transcription_cache:
        transcricao = transcription_cache[link]
        print("Transcrição obtida do cache.")
    else:
        # download do video
        video_path = baixar_video(link)
        
        # extracao do audio
        audio_path = extrair_audio(video_path)
        
        # transcrever audio
        transcricao = transcrever_audio(audio_path)
        transcription_cache[link] = transcricao
        print("Transcrição obtida do processamento.")
    
    print(transcricao)
    
    return "finish output"
    # executar agente1, analise da transcrição em busca da fobia
    # output = run_agent1(audio_path, fobia)
    
    # executar agente2, seleciona possiveis frames do video que contenham a fobia baseado na transcricao
    # output = run_agent2(output)
    
    # gera prints dos frames selecionados e classifica em um modelo BLIP
    # analisa_frames(output)
    
    # executar agente3, baseado no output dos agentes anteriores, gera um relatorio final
    # output = run_agent3(output)
    
    return "finish output"