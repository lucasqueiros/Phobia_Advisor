import streamlit as st
from run_pipeline import run_pipeline


#Interface do usuário
st.title("Análise de fobias em vídeos")
st.write("Insira o link do vídeo que deseja analisar")
link = st.text_input("Link do vídeo")
st.write("Insira a fobia que deseja analisar")
fobia = st.text_input("Fobia")

if st.button("Analisar"):
    st.write("Analisando...")
    output = run_pipeline(link, fobia)
    st.write(output)