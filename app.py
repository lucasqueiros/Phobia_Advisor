import streamlit as st
from run_pipeline import run_pipeline

# Interface do usuário
st.title("Análise de fobias em vídeos")
st.write("Insira o link do vídeo que deseja analisar:")
link = st.text_input("Link do vídeo", placeholder="Cole o link aqui...")
st.write("Insira a fobia que deseja analisar:")
fobia = st.text_input("Fobia", placeholder="Exemplo: aracnofobia")

# Verifica se ambos os campos estão preenchidos e se o botão foi clicado
if st.button("Analisar"):
    if not link or not fobia:
        st.error("Por favor, insira o link do vídeo e a fobia para prosseguir.")
    else:
        st.write("Analisando...")

        # Adiciona uma barra de progresso
        progress_bar = st.progress(0)
        try:
            # Chama a função do pipeline e atualiza o progresso
            for percent_complete in range(100):
                progress_bar.progress(percent_complete + 1)
            
            # Executa o pipeline apenas após o progresso ser completo
            output = run_pipeline(link, fobia)

            st.success("Análise concluída!")
            st.write(output)

        except Exception as e:
            st.error(f"Erro durante a análise: {str(e)}")
