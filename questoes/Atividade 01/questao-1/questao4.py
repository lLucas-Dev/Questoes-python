numero = int(input("Digite um número inteiro: "))

somar = 0

for i in range(1, numero):
  if (numero % i == 0):
    somar += i

if (somar == numero):
    print("O número é um número perfeito.")

else:
    print("O número não é um número perfeito.")