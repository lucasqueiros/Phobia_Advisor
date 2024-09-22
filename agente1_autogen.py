import autogen
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
api_key = os.getenv("API_KEY")

config_list = [{"model" : "gpt-3.5-turbo-16k", "api_key" : api_key}]

llm_config={
    "seed":42,
    "config_list":config_list,
    "temperature":0
}

assistant = autogen.AssistantAgent(
    name="Identificador de Frames",
    llm_config= llm_config,
    system_message= "Assistente audiovisual para identificação de frames relacionados a uma determinada fobia."
    )

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=1,
    is_termination_msg= lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config= {
        "work_dir" : "coding",
        "use_docker" : False,
    },
    llm_config=llm_config,
    system_message= """Reply TERMINATE if the task has been solved at full satisfaction.
    Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
    )

task = """
Você receberá uma transcrição de vídeo em formato de legenda e uma string que representa uma fobia. 
Procure em toda a transcrição palavras ou frases que possam estar diretamente ou indiretamente relacionados
com a fobia. Se encontrar identifique o tempo do vídeo em que a palavra ocorre e a palavra em sí.
Guarde o tempo e a palavra em um dicionario onde a chave é o tempo e o valor é a palavra.
Caso não encontre nenhuma palavra relacionada a fobia, divida o comprimento da transcrição e guarde 10 tempos no dicionario.
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)