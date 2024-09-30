import streamlit as st
from run_pipeline import run_pipeline

# Interface do usuário
st.title("Análise de fobias em vídeos")

# Input fields
link = st.text_input("Insira o link do vídeo que deseja analisar:", placeholder="Cole o link aqui...")
fobia = st.text_input("Insira a fobia que deseja analisar:", placeholder="Exemplo: aracnofobia")

# Botão de análise
if st.button("Analisar"):
    # Verificar se ambos os campos foram preenchidos
    if not link or not fobia:
        st.error("Por favor, insira tanto o link do vídeo quanto a fobia antes de analisar.")
    else:
        # Executar a análise apenas se o botão for pressionado
        with st.spinner('Analisando...'):
            try:
                resultado = run_pipeline(link, fobia)  # Chamada de função apenas quando o botão é clicado
                st.success('Análise concluída!')
                st.write("Resultado da análise:")
                st.write(resultado)
            except Exception as e:
                st.error(f"Ocorreu um erro durante a análise: {str(e)}")

# Adicionar informações adicionais
st.info("Esta aplicação analisa vídeos em busca de conteúdo relacionado a fobias específicas.")
st.write("Desenvolvido por Lucas Queirós")
