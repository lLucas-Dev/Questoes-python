arquivo = open("produto.csv", "r")
cabecalho = arquivo.readline()

soma_total = 0
quantidade_total = 0

for linha in arquivo:
    parte = linha.split(",")
    soma_total += float(parte[1])
    quantidade_total += 1

print(f"Soma total: {soma_total}")
print(f"Quantidade total: {quantidade_total}")

print(f"Média: {soma_total / quantidade_total}")