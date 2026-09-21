def contar_pares(n):
    count = 0
    for i in range(1, n + 1):
        if (i % 2 == 0):
            count += 1
    return count


numero = int(input("Digite um número inteiro: "))
quantidade_pares = contar_pares(numero)
print(f"A quantidade de números pares entre 1 e {numero} é: {quantidade_pares}")