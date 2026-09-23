sorteados = [5, 12, 23, 34, 45, 56]
usuario = [5, 10, 23, 30, 45, 60]
 
acertos = 0
for n in usuario:
    if n in sorteados:
        acertos += 1
 
print("Números em comum:", acertos)
 
