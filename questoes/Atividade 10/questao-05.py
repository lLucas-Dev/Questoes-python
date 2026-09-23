signos = {
    1: (20, "Capricórnio", "Aquário"),
    2: (19, "Aquário", "Peixes"),
    3: (21, "Peixes", "Áries"),
    4: (20, "Áries", "Touro"),
    5: (21, "Touro", "Gêmeos"),
    6: (21, "Gêmeos", "Câncer"),
    7: (23, "Câncer", "Leão"),
    8: (23, "Leão", "Virgem"),
    9: (23, "Virgem", "Libra"),
    10: (23, "Libra", "Escorpião"),
    11: (22, "Escorpião", "Sagitário"),
    12: (22, "Sagitário", "Capricórnio"),
}
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
corte, antes, depois = signos[mes]
print("Seu signo é:", antes if dia < corte else depois)