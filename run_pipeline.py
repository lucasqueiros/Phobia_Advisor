import baixar_video
import extrair_audio
import transcrever_audio

def run_pipeline(link, fobia):
    #download do video
    video_path = baixar_video(link)
     
    #extracao do audio
    audio_path = extrair_audio(video_path)
    
    #transcrever audio
    transcricao = transcrever_audio(audio_path)
    print(transcricao)
    
    return "finish output"
    #executar agente1, analise da transcrição em busca da fobia
    #output = run_agent1(audio_path, fobia)
    
    #executar agente2, seleciona possiveis frames do video que contenham a fobia baseado na transcricao
    #output = run_agent2(output)
    
    #gera prints dos frames selecionados e classifica em um modelo BLIP
    #analisa_frames(output)
    
    #executar agente3, baseado no output dos agentes anteriores, gera um relatorio final
    #output = run_agent3(output)
    
    return "finish output"