import streamlit as st  
import random
st.title("Desafio do número secreto")
if 'nummero_secreto' not in st.session_state:
    st.session_state.nummero_secreto = random.randint(1, 100)
numero_usuario = st.number_input("Digite um número entre 1 e 100:", min_value=1, max_value=100)
if 'qauntidade_tentativas' not in st.session_state:
    st.session_state.qauntidade_tentativas = 0
with st.sidebar:
    if st.button("Verificar"):
        st.session_state.qauntidade_tentativas += 1
        if numero_usuario < st.session_state.nummero_secreto:
            st.warning("O número secreto é maior!")

        elif numero_usuario > st.session_state.nummero_secreto:
            st.warning("O número secreto é menor!")
        else:
            st.success("Parabéns! Você acertou o número secreto!")
    if st.button("Novo jogo"):
        st.session_state.nummero_secreto = random.randint(1, 100)
        st.session_state.qauntidade_tentativas = 0
    st.write(f"Quantidade de tentativas: {st.session_state.qauntidade_tentativas}") 