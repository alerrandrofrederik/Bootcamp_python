import csv

def ler_csv(nome_arquivo: str) -> list:
    '''Função para ler o arquivo CSV
    '''
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)


def processar_dados(dados: list) -> dict:
    '''Função para processar os dados em um dicionário
    '''
    categorias = {}
    for item in dados:
        categoria = item['Categoria']
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias


def calcular_vendas_categoria(dados:dict)-> dict:
    '''Função para calcular o total de vendas por categoria
    '''
    vendas_por_categoria = {}
    for categoria, itens in dados.items():
        total_vendas = sum(int(item['Quantidade']) * int(item['Venda']) for item in itens)
        vendas_por_categoria[categoria] = total_vendas
    return vendas_por_categoria


def main():
    '''Função principal para integrar as funções anteriores
    '''
    nome_arquivo = 'Aula_07/vendas.csv'
    dados_brutos = ler_csv(nome_arquivo)
    dados_processados = processar_dados(dados_brutos)
    vendas_categoria = calcular_vendas_categoria(dados_processados)
    for categoria, total in vendas_categoria.items():
        print(f'{categoria}: ${total}')

if __name__ == '__main__':
    main()