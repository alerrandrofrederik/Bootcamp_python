# Pergunta: olhando para a estrutura da lista vendas, que contém dicionários com chave string 
# e valores que podem ser str, int ou float, como você colocaria o type hint dessa variável?

# (Dica: vai precisar usar List, Dict e talvez Union do módulo typing).

vendas = [
    {"produto": "arroz", "quantidade": 2, "preco": 20.0},
    {"produto": "feijão", "quantidade": 1, "preco": 8.0},
    {"produto": "macarrão", "quantidade": 3, "preco": 5.0},
]

from typing import List, Dict, Union

vendas: List[Dict[str, Union[str, int, float]]] = [
    {"produto": "arroz", "quantidade": 2, "preco": 20.0},
    {"produto": "feijão", "quantidade": 1, "preco": 8.0},
    {"produto": "macarrão", "quantidade": 3, "preco": 5.0},
]
