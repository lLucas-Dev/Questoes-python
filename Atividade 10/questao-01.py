frase = input("Digite uma frase: ")
frequencia = {}
for palavra in frase.split():
    frequencia[palavra] = frequencia.get(palavra, 0) + 1
print(frequencia)
