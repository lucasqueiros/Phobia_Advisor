import moviepy.editor as mp

video_path = "/home/lucasqueiros/Documentos/Phobia_Advisor/data/video"

def extrair_audio(video_path):
    audio = mp.VideoFileClip(video_path).audio
    audio_path = 'data/audio.mp3'
    audio.write_audiofile(audio_path)
    return audio_path

extrair_audio(video_path)