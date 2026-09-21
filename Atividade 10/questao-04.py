convidados = {}
while True:
    nome = input("Nome do convidado (vazio para terminar): ")
    if nome == "":
        break
    convidados[nome] = convidados.get(nome, 0) + 1
print(convidados)
