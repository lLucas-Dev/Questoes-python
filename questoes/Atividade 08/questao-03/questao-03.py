from datetime import datetime

def tempo():
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y")
    with open("texto.txt", "a") as arquivo:
        arquivo.write(f"\nData de execução: {data_formatada}\n")
    

quantidade = 0

with open("texto.txt", "r") as texto:
    conteudo = texto.read()
    quantidade = len(conteudo.split())

print(f"A quantidade de palavras no arquivo é: {quantidade}")
tempo()

