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
        
        # extracao do audio
        audio_path = extrair_audio(video_path)
        
        # transcrever audio
        transcricao = transcrever_audio(audio_path)
        
        lista_frames = lista_frames(transcricao, fobia)
        
        capture_frames(video_path, lista_frames)
        
        processar_imagens('data/frames/', 'data/legendas.txt')
        
        return analise_final.decisao_llm(lista_frames, transcricao, fobia)
    
