import json

def add_produto(nome, quantidade):
    produto = {"nome": nome, "quantidade": quantidade}
    inventario.append(produto)
    with open("inventario.json", "w") as arquivo_json:
        json.dump(inventario, arquivo_json, indent=2)
    print(f"Produto {nome} adicionado com sucesso!")

def listar_produtos():
    print("\nProdutos no inventário:")
    for produto in inventario:
        print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}")

def remover_produto(nome):
    for produto in inventario:
        if produto["nome"] == nome:
            inventario.remove(produto)
            with open("inventario.json", "w") as arquivo_json:
                json.dump(inventario, arquivo_json, indent=2)
            print(f"Produto {nome} removido com sucesso!")
            return
    print(f"Produto {nome} não encontrado no inventário.")

inventario = [
    {"nome": "Arroz", "quantidade": 50},
    {"nome": "Feijao", "quantidade": 30},
    {"nome": "oleo", "quantidade": 20}
]

arquivo_json = open("inventario.json", "w")
json.dump(inventario, arquivo_json, indent = 2)
print("Arquivo JSON criado com sucesso!")

while True:
    print("\nMenu:")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Remover produto")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_produto = input("Digite o nome do produto: ")
        quantidade_produto = int(input("Digite a quantidade do produto: "))
        add_produto(nome_produto, quantidade_produto)
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        nome_produto = input("Digite o nome do produto a ser removido: ")
        remover_produto(nome_produto)   
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
