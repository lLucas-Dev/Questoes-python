def somar_multiplos(n):
    somar = 0
    for i in range(1,n+1):
        if (i % 3 == 0 or i % 5 == 0):
            somar += i
    return somar


numero = int(input("Digite um número inteiro: "))
resultado = somar_multiplos(numero)
print(f"A soma dos múltiplos de 3 ou 5 entre 1 e {numero} é: {resultado}")