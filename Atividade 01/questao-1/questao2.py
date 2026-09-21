numero = int (input("Digite um numero:"))

for i in range(2, numero):
    if (numero % i) == 0:
        print ("O numero não é primo")
        break

if(numero % i) != 0:
    print ("O numero é primo")

