def estatisticas (*args):
    somar = sum(args)
    media = somar / len(args)
    maior = max(args)
    menor = min(args)
    return somar, media, maior, menor

numero_lista = []
while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")
    if numero.lower() == 'sair':
        break
    numero_lista.append(float(numero))
resultado = estatisticas(*numero_lista)
print (resultado)