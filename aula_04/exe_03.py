
usuarios: List[Dict[str, Union[int, str, int, list[float]]]] = [
    {"id": 1, "nome": "Maria", "idade": 28, "compras": [120.5, 55.0, 89.9]},
    {"id": 2, "nome": "João", "idade": 35, "compras": [300.0]},
    {"id": 3, "nome": "Ana", "idade": 22, "compras": []},
]

for usuario in usuarios:
    nome = usuario["nome"]
    idade = usuario["idade"]
    total_compras = sum(usuario["compras"])

    print("O usuário ", nome, "tem ", idade, "de idade e comprou um total de ", total_compras)