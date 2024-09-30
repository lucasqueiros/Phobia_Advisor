import cv2
from PIL import Image

def capture_frames(video_path, timestamps):
    print(timestamps)
    print(type(timestamps))    
    print ("Capturando frames...")
    # Abrir o vídeo
    video = cv2.VideoCapture(video_path)
    
    
    # Iterar sobre os timestamps
    for i, timestamp in enumerate(timestamps):
        # Definir a posição do vídeo para o timestamp desejado
        video.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)
        
        # Ler o frame
        ret, frame = video.read()
        
        if ret:
            # Converter o frame de BGR para RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Criar uma imagem PIL a partir do frame
            img = Image.fromarray(frame_rgb)
            
            # Salvar a imagem
            img.save(f"data/frame_{i+1}.png")
            print(f"Frame capturado em {timestamp} segundos e salvo como frame_{i+1}.png")
        else:
            print(f"Não foi possível capturar o frame em {timestamp} segundos")
    
    # Liberar o objeto de vídeo
    video.release()
