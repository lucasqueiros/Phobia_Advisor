import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Carregar o modelo e o processador (já definidos no código do usuário)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Caminho da pasta com as imagens (já definido no código do usuário)
path = "data/frames/"

# Função para legendar imagem (já definida no código do usuário)
def legendar_imagem(image):
    inputs = processor(image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

def processar_imagens(pasta, arquivo_saida):
    # Abrir o arquivo de saída
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        # Iterar sobre todas as imagens na pasta
        for filename in os.listdir(pasta):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_path = os.path.join(pasta, filename)
                
                try:
                    # Carregar a imagem
                    image = Image.open(image_path).convert('RGB')
                    
                    # Gerar a legenda
                    caption = legendar_imagem(image)

                    # Escrever o nome do arquivo e a legenda no arquivo de saída
                    f.write(f"Arquivo: {filename}\n")
                    f.write(f"Legenda: {caption}\n\n")
                    
                    print(f"Legenda gerada para {filename}")
                except Exception as e:
                    print(f"Erro ao processar {filename}: {str(e)}")

    print(f"Legendas salvas em {arquivo_saida}")

# Exemplo de uso
arquivo_saida = "data/legendas.txt"

processar_imagens(path, arquivo_saida)