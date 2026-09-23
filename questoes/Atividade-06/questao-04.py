def calculadora(num1,num2,operacao): 
    match operacao:
        case "soma":
            return num1 + num2
        case "subtracao":
            return num1 - num2
        case "multiplicacao":
            return num1 * num2
        case "divisao":
            if num2 != 0:
                return num1 / num2
            else:
                return "Erro: Divisão por zero não é permitida." 

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
print("Escolha a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = input("Digite o da operação: ")
resultado = calculadora(numero1, numero2, opcao)
print(f"O resultado da operação é: {resultado}")