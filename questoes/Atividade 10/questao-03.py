carrinho = {}
while True:
    produto = input("Produto (vazio para terminar): ")
    if produto == "":
        break
    quantidade = int(input("Quantidade: "))
    carrinho[produto] = quantidade
print(carrinho)