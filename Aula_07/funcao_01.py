# %%

idades = [18,32,24,36]

# Quantidade = len(idades)
# soma = sum (idades)
# Quantidade
# soma
# media = soma / Quantidade
# media

# %%
def media_idade(idade: list) -> float:
    '''
        Função que calcula a média de idade a partir de uma lista
    '''
    Quantidade = len(idades)
    soma = sum(idades)
    resultado = soma / Quantidade
    return resultado

# %%
print(type(media_idade(idades)))