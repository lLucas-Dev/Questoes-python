alunos = []

for i in range(2):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos.append((nome,nota))

maior = max(alunos, key=lambda x: x[1])
print (f"maior nota é de {maior[0]} com {maior[1]}")