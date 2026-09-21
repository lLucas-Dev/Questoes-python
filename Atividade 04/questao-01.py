from dataclasses import dataclass

@dataclass
class pessoa:
    nome: str
    idade: int
    altura: float
    estudante: bool
    hobbies: list[str]


while True:
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    altura = float(input("Digite a altura da pessoa (em metros): "))
    estudante_input = input("A pessoa é estudante? (sim/não): ").strip().lower()
    estudante = estudante_input == "sim"
    hobbies_input = input("Digite os hobbies da pessoa, separados por vírgula: ")
    hobbies = [hobby.strip() for hobby in hobbies_input.split(",")]

    pessoa1 = pessoa(nome, idade, altura, estudante, hobbies)

    print("\nInformações da pessoa cadastrada:")
    print(f"Nome: {pessoa1.nome}")
    print(f"Idade: {pessoa1.idade}")
    print(f"Altura: {pessoa1.altura} m")
    print(f"Estudante: {'Sim' if pessoa1.estudante else 'Não'}")
    print(f"Hobbies: {', '.join(pessoa1.hobbies)}")

    continuar = input("\nDeseja cadastrar outra pessoa? (sim/não): ").strip().lower()
    if continuar != "sim":
        break

    