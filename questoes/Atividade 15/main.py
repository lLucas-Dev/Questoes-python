from fastapi import FastAPI
from pydantic import BaseModel
import json 

ARQUIVOS = "tarefas.json"

app = FastAPI()
nova_tarefa = {
    "id": 4,
    "tarefa": "Estudar FastAPI",
    "status": "Pendente"
}

def ler_arquivo():
    with open(ARQUIVOS, "r", encoding="utf-8") as arquivo:
        tarefas = json.load(arquivo)
    return tarefas

def escrever_arquivo(tarefas):
    with open(ARQUIVOS, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

@app.get("/tarefas")
def listar_tarefas():
    tarefas = ler_arquivo()
    return tarefas

class Tarefa_nova(BaseModel):
    tarefa: str
    status: str

@app.post("/tarefas")
def adicionar_tarefa(tarefa: Tarefa_nova):
    tarefas = ler_arquivo()
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "tarefa": tarefa.tarefa,
        "status": tarefa.status
    }
    tarefas.append(nova_tarefa)
    escrever_arquivo(tarefas)
    return {"message": "Tarefa adicionada com sucesso", "tarefa": nova_tarefa}

@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa: Tarefa_nova):
    tarefas = ler_arquivo()
    for t in tarefas:
        if t["id"] == tarefa_id:
            t["tarefa"] = tarefa.tarefa
            t["status"] = tarefa.status
            escrever_arquivo(tarefas)
            return {"message": "Tarefa atualizada com sucesso", "tarefa": t}
    return {"message": "Tarefa não encontrada"}

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    tarefas = ler_arquivo()
    for t in tarefas:
        if t["id"] == tarefa_id:
            tarefas.remove(t)
            escrever_arquivo(tarefas)
            return {"message": "Tarefa deletada com sucesso"}
    return {"message": "Tarefa não encontrada"}
