
vendas = [
    {"produto": "arroz", "quantidade": 2, "preco": 20.0},
    {"produto": "feijão", "quantidade": 1, "preco": 8.0},
    {"produto": "macarrão", "quantidade": 3, "preco": 5.0},
]

for venda in vendas:
    produto = venda["produto"]
    total = venda["quantidade"] * venda["preco"]
    print("O valor total do produto ", produto, "foi:", total)
