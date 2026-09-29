import streamlit as st

st.title("Portal turistico")

st.image("maxresdefault.jpg", caption="Foto de parnaiba")

with st.sidebar:
    st.write("Conheça os melhores destinos!")
    st.link_button("Destinos", "#")
    st.link_button("Galeria", "#")
    st.link_button("Materiais", "#")
    st.link_button("Links", "#")
    st.link_button("Contato", "#")
    st.link_button("Avaliação", "#")
     