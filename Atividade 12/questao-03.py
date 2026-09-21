class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome}!")

familia = [Pessoa("Ana", 40), Pessoa("Carlos", 42), Pessoa("Lucas", 20)]

def todos_falam(lista):
    for pessoa in lista:
        pessoa.falar()

todos_falam(familia)