import json

dados = """
{
  "loja": "TechStore",
  "produtos": [
    {
      "id": 1,
      "nome": "Teclado",
      "categoria": "Periféricos",
      "preco": 120.00,
      "estoque": 15
    },
    {
      "id": 2,
      "nome": "Mouse",
      "categoria": "Periféricos",
      "preco": 80.00,
      "estoque": 5
    }
  ]
}
"""

dado = json.loads(dados)
somar = 0
for produto in dado["produtos"]:
    print(f"Produto: {produto['nome']}") 
    if (produto["estoque"] < 6):
        print(f"Produto {produto['nome']} está com estoque baixo: {produto['estoque']} unidades.")

for produto in dado["produtos"]:
    valor_total = produto["preco"] * produto["estoque"]
    print(f"Valor total em estoque do produto {produto['nome']}: R${valor_total:.2f}")

for produto in dado["produtos"]:
    somar += produto["estoque"]

print(f"Quantidade total de produtos em estoque: {somar} unidades.")

print(f"Produto com maior valor em estoque é: {max(dado['produtos'], key=lambda x: x['preco'] * x['estoque'])['nome']}")