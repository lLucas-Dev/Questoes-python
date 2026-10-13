import streamlit as st
import requests
import json

st.title("Gerenciador de Tarefas")

response = requests.get("http://localhost:8000/tarefas")
tarefas = response.json()
st.write("Tarefas Atuais")
escolha = st.selectbox("Lista de Tarefas", tarefas, format_func=lambda x: f"{x['id']}: {x['tarefa']} - {x['status']}")

st.radio("Ação", ["Adicionar Tarefa", "Atualizar Tarefa", "Deletar Tarefa"], key="acao")

match st.session_state.acao:
    case "Adicionar Tarefa":
        with st.form("Adicionar Tarefa"):
            tarefa = st.text_input("Tarefa", placeholder="Digite a tarefa")
            status = st.selectbox("Status", ["Pendente", "Concluída"])
            if st.form_submit_button("Adicionar"): 
                nova_tarefa = {"tarefa": tarefa, "status": status}
                response = requests.post("http://localhost:8000/tarefas", json=nova_tarefa)
                if response.status_code == 200:
                    st.success("Tarefa adicionada com sucesso!")
                else:
                    st.error("Erro ao adicionar tarefa.")
    case "Atualizar Tarefa":
        with st.form("Atualizar Tarefa"):
            tarefa = st.text_input("Nova tarefa", placeholder="Digite a nova tarefa")
            status = st.selectbox("Status", ["Pendente", "Concluída"])
            if st.form_submit_button("Atualizar"): 
                response = requests.put(f"http://localhost:8000/tarefas/{escolha['id']}", json={"tarefa": tarefa, "status": status})
                if response.status_code == 200:
                    st.success("Tarefa atualizada com sucesso!")
                else:
                    st.error("Erro ao atualizar tarefa.")   
    case "Deletar Tarefa":
        if st.button("Deletar"):
            response = requests.delete(f"http://localhost:8000/tarefas/{escolha['id']}")
            if response.status_code == 200:
                st.success("Tarefa deletada com sucesso!")
            else:
                st.error("Erro ao deletar tarefa.")