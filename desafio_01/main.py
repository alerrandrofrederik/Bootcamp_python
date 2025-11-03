import csv

arquivo = 'funcionarios.csv'

def get_csv(path_arquivo: str) -> dict:
    '''Funão para ler o arquivo csv de Funcionários.csv

    parametros: 
        path_arquivo: caminho do arquivo csv
    '''
    with open(path_arquivo, mode='r', encoding='utf-8') as file:
        leitor = csv.DictReader(file)

        funcionario = [
            {
                'id':(linha['id']),
                'nome':(linha['nome']),
                'area':(linha['area']),
                'salario':int(linha['salario']),
                'bonus_percentual':(linha['bonus_percentual'])
            }
            for linha in leitor
        ]

        return funcionario


def main():
    '''Função principal para integrar as funções anteriores
    '''
    nome_arquivo = 'desafio_01/funcionarios.csv'
    dados = get_csv(nome_arquivo)
    print(dados)
    # dados_brutos = ler_csv(nome_arquivo)
    # dados_processados = processar_dados(dados_brutos)
    # vendas_categoria = calcular_vendas_categoria(dados_processados)
    # for categoria, total in vendas_categoria.items():
    #     print(f'{categoria}: ${total}')

if __name__ == '__main__':
    main()