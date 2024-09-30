from baixar_video import baixar_video
from extrair_audio import extrair_audio
from transcrever_audio import transcrever_audio
from lista_frames import lista_frames
from gerar_prints import capture_frames
from BLIP_model import processar_imagens
import analise_final
import os
import json
import atexit


def run_pipeline(link, fobia):
        # download do video
        video_path = baixar_video(link)
        
        print("video baixado")
        
        # extracao do audio
        audio_path = extrair_audio(video_path)
        
        print("audio extraido")
        
        # transcrever audio
        transcricao = transcrever_audio(audio_path)
        
        print("transcrição feita")
        
        frames_list = lista_frames(transcricao, fobia)
        
        print("lista deframes e resumo feitos")
        
        capture_frames(video_path, frames_list)
        
        print("frames capturados")
        
        processar_imagens('data/frames/', 'data/legendas.txt')
        
        print("imagens processadas no modelo blip")
        
        return analise_final.decisao_llm(frames_list, transcricao, fobia)
    
    
    
