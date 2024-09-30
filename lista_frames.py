import openai
from dotenv import load_dotenv, find_dotenv

# Carrega variáveis de ambiente do arquivo .env
_ = load_dotenv(find_dotenv())



# Função para buscar frames que correspondem à fobia
def lista_frames(conteudo, fobia):
    # Prompt a ser enviado para o ChatGPT
    prompt = f"""Analise a transcrição abaixo em busca da palavra '{fobia}' ou termos relacionados. 
    A transcrição está em formato de legenda .srt. Gere uma lista python com os segundos do vídeo onde a palavra '{fobia}' 
    ou termos relacionados aparecem. Tambem gere breve resumo do
    ####
    {conteudo}
    ####"""
    
    # Chamada da API da OpenAI
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Obtém o conteúdo da resposta
    resposta = response.choices[0].message.content
    
    # Salva a resposta em um arquivo .txt
    with open('data/resumo.txt', 'w') as file:
        file.write(resposta)
    
    return resposta  # Retorna a resposta processada da API

