import requests

pares = {
    "1": ("BRL-USD", "BRLUSD"),
    "2": ("EUR-USD", "EURUSD"),
    "3": ("BTC-USD", "BTCUSD"),
    "4": ("BTC-BRL", "BTCBRL"),
}

while True:
    print("\n===== COTAÇÃO =====")
    print("1 - BRL / USD")
    print("2 - EUR / USD")
    print("3 - BTC / USD")
    print("4 - BTC / BRL")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        break
    if opcao not in pares:
        print("Opção inválida!")
        continue

    par, chave = pares[opcao]
    url = "https://economia.awesomeapi.com.br/json/last/" + par
    dados = requests.get(url).json()
    print(f"{par}: {dados[chave]['bid']}")
