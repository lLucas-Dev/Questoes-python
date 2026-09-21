class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 
    def ligar(self):
        print(f"O carro {self.marca} {self.modelo} está ligado.")
 
class Eletrico(Carro):
    def ligar(self):
        print(f"O carro elétrico {self.marca} {self.modelo} está ligado silenciosamente.")
 
carro = Carro("Fiat", "Uno")
eletrico = Eletrico("Tesla", "Model 3")
carro.ligar()
eletrico.ligar()
    