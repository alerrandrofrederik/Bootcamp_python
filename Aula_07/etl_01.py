
# %%
# 1.Ler CSV:
import csv

arquivo = 'vendas.csv'

with open(arquivo, mode='r', encoding='utf-8') as file:
    leitor = csv.DictReader(file)

    vendas = [
        {
            'Produto': str(venda['Produto']),
            'Categoria': str(venda['Categoria']),
            'Quantidade': int(venda['Quantidade']),
            'vl_Venda': float(venda['Venda']),
            'total_venda': int(venda['Quantidade']) * float(venda['Venda'])
        }
        for venda in leitor
    ]

vendas
# %%
# 2.Processar Dados:

chaves = [i['Categoria'] for i in vendas]
chaves = set(chaves) # mantem valores unicos
chaves = list(chaves) # tranf. em lista para poder navegar nos itens
## crir lista de dicionarios com as categorias
vendas_por_categorias = dict()
for c in chaves:
    vendas_por_categorias[c] = []
## preenche os dicionários separando por categoria
for item in vendas:
    for c in chaves:
        if item['Categoria'] == c:
            vendas_por_categorias[c].append(item)

vendas_por_categorias

# %%
# 3.Calcular Vendas por Categoria primeira forma:
total_por_categoria = {}
for categoria, itens_venda in vendas_por_categorias.items():
    # Inicializa o total para a categoria atual
    total_vendas = 0
    # Itera sobre a lista de dicionários para cada categoria
    for item in itens_venda:
        # Acumula o valor de 'total_venda' de cada item
        total_vendas += item['total_venda']
    # Atribui a soma total ao dicionário de resultados
    total_por_categoria[categoria] = total_vendas

print(total_por_categoria)
# %%
# 3.Calcular Vendas por Categoria segunda forma:
total_por_categoria = {}
for categoria, itens_venda in vendas_por_categorias.items():
    total_por_categoria[categoria] = sum(item['total_venda'] 
                                         for item in itens_venda)

print(total_por_categoria)
