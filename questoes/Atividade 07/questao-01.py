import json


dados_json = """
[
    {"nome": "Ana", "idade": 20, "curso": "ADS", "notas": [8.0, 7.5, 9.0]},
    {"nome": "Carlos", "idade": 22, "curso": "ADS", "notas": [5.0, 6.0, 7.5]},
    {"nome": "Mariana", "idade": 21, "curso": "ADS", "notas": [9.0, 9.5, 9.0]},
    {"nome": "Pedro", "idade": 23, "curso": "ADS", "notas": [7.0, 7.0, 7.5]}
]
"""


alunos = json.loads(dados_json)
alunos_aprovados = []
media_alunos = []
for aluno in alunos:
    soma = sum(aluno["notas"])
    quantidade = len(aluno["notas"])
    media = soma / quantidade
    print(f"Aluno: {aluno['nome']}, Média: {media:.2f}")
    media_alunos.append(media)
    if(media >= 7.0):
        alunos_aprovados.append(aluno["nome"])

print("\nAlunos aprovados:")

for aluno in alunos_aprovados:
    print(f"Aluno aprovado: {aluno}")

print("\n")

print(f"Maior média: {max(media_alunos):.2f}")