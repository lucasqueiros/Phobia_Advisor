import gradio as gr
from run_pipeline import run_pipeline

# Função que será chamada ao clicar no botão de análise
def analisar_fobia(link, fobia):
    if not link or not fobia:
        return "Erro: Por favor, insira tanto o link do vídeo quanto a fobia."
    
    try:
        resultado = run_pipeline(link, fobia)
        return f"Análise concluída!\n\nResultado: {resultado}"
    except Exception as e:
        return f"Ocorreu um erro durante a análise: {str(e)}"

# Interface do Gradio
demo = gr.Interface(
    fn=analisar_fobia,  # Função que será executada
    inputs=[
        gr.Textbox(label="Insira o link do vídeo que deseja analisar:", placeholder="Cole o link aqui..."),
        gr.Textbox(label="Insira a fobia que deseja analisar:", placeholder="Exemplo: aracnofobia")
    ],
    outputs="text",  # Resultado será exibido como texto
    title="Análise de Fobias em Vídeos",
    description="Esta aplicação analisa vídeos em busca de conteúdo relacionado a fobias específicas."
)

# Iniciar a aplicação
if __name__ == "__main__":
    demo.launch()
