import csv

arquivo = 'funcionarios.csv'

def get_csv(path_arquivo: str) -> dict:
    '''Funão para ler o arquivo csv de Funcionários.csv
    e processar em uma lista de dcioários

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

def valida_dados(dados: list) -> dict:
    '''Fnção que aplica regras de validação no arquivo Funcionários.csv
    
        Parâmetros:
            dados (list): lista de dicionários contendo os dados de funcionários.
    
        Retorna:
            dict: dicionário com duas listas — 'com_erro' e 'sem_erro'.
    '''
    com_erro = []
    sem_erro = []

    for i in dados:
        try:
            #valida nome
            if len(i['nome']) == 0:
                i['erro'] = 'Nome vazio'
                com_erro.append(i)
            elif any(char.isdigit() for char in i['nome']):
                i['erro'] = 'Nome contém numeros'
                com_erro.append(i)

            #valida Area:
            elif i['area'] not in ('Vendas','TI','Financeiro','RH','Operações'):
                i['erro'] = 'area fora do esperado'
                com_erro.append(i)

            #valida Salário:
            elif not isinstance(i['salario'], int):
                i['erro'] = 'Tipo salario não válido'
                com_erro.append(i)
            elif i['salario'] < 0:
                i['erro'] = 'Salario negativo'
                com_erro.append(i)

            #valida bonus_percentual:
            elif len(i['bonus_percentual']) == 0:
                i['erro'] = 'bonus_percentual vazio'
                com_erro.append(i)
            elif not 0 <= float(i['bonus_percentual']) <= 1:
                i['erro'] = 'bonus_percentual fora do intervalo esperado'
                com_erro.append(i)

            else:
                BONUS_BASE = 1000
                salario = float(i['salario'])
                bonus_percentual = float(i['bonus_percentual'])
                i['bonus_final'] = BONUS_BASE + salario * bonus_percentual
                sem_erro.append(i)
        except ValueError:
            i['erro'] = 'valor invalido check os valores'
            com_erro.append(i)

        # resultado_validacao = {'com_erro': com_erro, 'sem_erro': sem_erro}
        
    return {'com_erro': com_erro, 'sem_erro': sem_erro}

def get_funcionarios_validos_por_area(dados_validos: dict) -> dict:
    '''Função para criar dicionários de funcionarios por area a partir do dicionário validado

    Parametro: 
        Dicionário de funcioários validados

    Retorna:
        Dict: Dicionário de funcionários por area
    '''
    funcionarios_por_area = {}
    chaves = list(set([i['area'] for i in dados_validos]))

    for c in chaves:
        funcionarios_por_area[c] = []

    for linha in dados_validos:
        for c in chaves:
            if linha['area'] == c:
                funcionarios_por_area[c].append(linha)


    return funcionarios_por_area


def total_funcionarios_por_area(dados_funcioarios: dict) -> dict:
    '''Função para calcular a quantidade de funcionários por are

    Parametros:
        dados_funcioarios: Dicionário de Funcoários por area

    return:
        Quantidade de funcionários por area
    '''
    qtd_funcionarios_por_area = {area: len(funcionarios) for area, funcionarios in dados_funcioarios.items()}

    return qtd_funcionarios_por_area

def main():
    '''Função principal para integrar as funções anteriores
    '''
    nome_arquivo = 'desafio_01/funcionarios.csv'
    dados_brutos = get_csv(nome_arquivo)
    dados_validacao = valida_dados(dados_brutos)
    funcionarios_area = get_funcionarios_validos_por_area(dados_validacao['sem_erro'])
    funcionarios_area_qtd = total_funcionarios_por_area(funcionarios_area)
    print(funcionarios_area_qtd)
    # dados_brutos = ler_csv(nome_arquivo)
    # dados_processados = processar_dados(dados_brutos)
    # vendas_categoria = calcular_vendas_categoria(dados_processados)
    # for categoria, total in vendas_categoria.items():
    #     print(f'{categoria}: ${total}')

if __name__ == '__main__':
    main()