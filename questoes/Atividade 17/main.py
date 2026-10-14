import json
import random

with open ("alunos.json", "r") as f:
    alunos = json.load(f)

alunos.append("Pedro")

with open("alunos.json", "w") as f:
    json.dump(alunos, f, indent=4)

print(random.choice(alunos))
print(random.sample(alunos, 3))
random.shuffle(alunos)
print(alunos)

