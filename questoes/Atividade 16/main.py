import streamlit as st
import requests

request = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()
st.session_state.deck_id = request["deck_id"]

def puxar_carta():
    deck_id = st.session_state.deck_id
    draw_card = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2").json()
    return draw_card["cards"]

st.title("Carta Aleatória")

if st.button("Puxar Carta"):
    carta = puxar_carta()
    col1, col2 = st.columns(2)
    with col1:
        st.image(carta[0]["image"])
    with col2:
        st.image(carta[1]["image"])


