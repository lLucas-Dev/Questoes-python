numero = int(input("Digite um número inteiro: "))


somar = 0
while numero > 0:
    digito = numero % 10
    somar += digito ** 2
    numero // 10
print("A soma dos quadrados dos dígitos é:", somar)