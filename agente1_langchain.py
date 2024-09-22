import re
from typing import List, Tuple
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.prompts import StringPromptTemplate
from langchain import OpenAI, LLMChain
from langchain.schema import AgentAction, AgentFinish

def parse_srt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def analyze_subtitles(input_str: str) -> str:
    file_path, search_word = input_str.split(',')
    subtitle_content = parse_srt(file_path.strip())
    return subtitle_content

tools = [
    Tool(
        name="GetSubtitleContent",
        func=analyze_subtitles,
        description="Obtém o conteúdo do arquivo de legendas .srt. Entrada: 'caminho_do_arquivo.srt, palavra_a_procurar'"
    )
]

template = """Você é um assistente especializado em análise de legendas. Analise o conteúdo da legenda fornecido e encontre todas as ocorrências da palavra especificada, incluindo palavras relacionadas semanticamente.

{tools}

Use o seguinte formato:

Pergunta: a pergunta de entrada
Pensamento: você deve sempre pensar sobre o que fazer
Ação: a ação a tomar, deve ser uma das ferramentas [{tool_names}]
Entrada da Ação: a entrada para a ação
Observação: o resultado da ação
Pensamento: Agora vou analisar o conteúdo da legenda
Análise: Faça uma análise detalhada do conteúdo da legenda, procurando pela palavra especificada e palavras relacionadas
Resposta Final: Forneça um resumo das ocorrências encontradas, incluindo as minutagens e o contexto

Pergunta: {input}
{agent_scratchpad}"""

class CustomPromptTemplate(StringPromptTemplate):
    template: str
    tools: List[Tool]

    def format(self, **kwargs) -> str:
        intermediate_steps = kwargs.pop("intermediate_steps")
        thoughts = ""
        for action, observation in intermediate_steps:
            thoughts += action.log
            thoughts += f"\nObservação: {observation}\nPensamento: "
        kwargs["agent_scratchpad"] = thoughts
        kwargs["tools"] = "\n".join([f"{tool.name}: {tool.description}" for tool in self.tools])
        kwargs["tool_names"] = ", ".join([tool.name for tool in self.tools])
        return self.template.format(**kwargs)

prompt = CustomPromptTemplate(
    template=template,
    tools=tools,
    input_variables=["input", "intermediate_steps"]
)

class CustomOutputParser:
    def parse(self, llm_output: str) -> AgentAction or AgentFinish:
        if "Resposta Final:" in llm_output:
            return AgentFinish(
                return_values={"output": llm_output.split("Resposta Final:")[-1].strip()},
                log=llm_output,
            )
        
        action_match = re.search(r"Ação\s*:\s*(.*?)\nEntrada da Ação\s*:\s*(.*)", llm_output, re.DOTALL)
        if not action_match:
            raise ValueError(f"Não foi possível analisar a saída do LLM: `{llm_output}`")
        action = action_match.group(1).strip()
        action_input = action_match.group(2)
        return AgentAction(tool=action, tool_input=action_input.strip(" ").strip('"'), log=llm_output)

llm = OpenAI(temperature=0)
llm_chain = LLMChain(llm=llm, prompt=prompt)
tool_names = [tool.name for tool in tools]
agent = LLMSingleActionAgent(
    llm_chain=llm_chain, 
    output_parser=CustomOutputParser(),
    stop=["\nObservação:"], 
    allowed_tools=tool_names
)

agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__":
    result = agent_executor.run("Analise o arquivo 'exemplo.srt' e encontre todas as ocorrências da palavra 'importante' e palavras semanticamente relacionadas.")
    print(result)