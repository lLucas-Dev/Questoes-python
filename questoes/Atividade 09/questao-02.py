usuario = []
 
while len(usuario) < 6:
    numero = int(input(f"Digite o número {len(usuario) + 1} (1 a 60): "))
    if numero < 1 or numero > 60:
        print("Número inválido! Escolha entre 1 e 60.")
    elif numero in usuario:
        print("Você já escolheu esse número!")
    else:
        usuario.append(numero)
 
print("Seus números:", sorted(usuario))
