import moviepy.editor as mp

def extrair_audio(video_path):
    audio = mp.VideoFileClip(video_path).audio
    audio_path = 'data/audio.mp3'
    audio.write_audiofile(audio_path)
    return audio_path
