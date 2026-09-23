
try:
    with open ("contador.txt", "r") as arquivo: 
        conteudo = arquivo.read()
    if(conteudo == ""):
        quantide = 0
    else:
        quantide = int(conteudo)
except FileNotFoundError:
    quantide = 0


with open ("contador.txt", "w") as arquivo:
    quantide += 1
    arquivo.write(str(quantide))

print(f"Este sistema já foi acessado {quantide} vezes.")