medias = {}
qtd = int(input("Quantos alunos? "))
for i in range(qtd):
    nome = input("Nome do aluno: ")
    notas = input("Notas separadas por espaço: ").split()
    notas = [float(n) for n in notas]
    medias[nome] = sum(notas) / len(notas)
print(medias)