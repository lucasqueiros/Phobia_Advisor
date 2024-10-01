import openai
from dotenv import load_dotenv, find_dotenv

# Carrega variáveis de ambiente do arquivo .env
_ = load_dotenv(find_dotenv())

with open('data/resumo.txt', 'r', encoding='utf-8') as file:
    resumo = file.read()

with open('data/legendas.txt', 'r', encoding='utf-8') as file:
    legenda = file.read()


def decisao_llm(resumo, legenda, fobia):
    prompt = f"""Baseado no resumo e na legenda dos frames analisados, tome uma decisão sobre se o usuario
    pode assistir ao video ou não sabendo que ele tem fobia de {fobia}. O resumo contem um breve texto do conteudo do video alem de uma lista de tempos.
    A legenda tem textos gerados a partir dos frames dos tempos criados no resumo. Gere um texto explicando a decisão.
    Caso a decisão seja positiva, explique porque o usuário pode assistir ao vídeo citando o possivel tempo do video em que a fobia aparece. 
    ####
    {resumo}
    ####
    ####
    {legenda}
    #####
    Pense passo a passo. Primeiro, analise o resumo e a legenda e tome uma decisão."""

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )

    resposta = response.choices[0].message.content

    with open('data/decisao.txt', 'w', encoding='utf-8') as file:
        file.write(resposta)

    return resposta