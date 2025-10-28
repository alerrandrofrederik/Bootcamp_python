
# %%
import csv

arquivo = 'funcionarios.csv'

with open(arquivo, mode='r', encoding='utf-8') as file:
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

funcionario
# %%
com_erro = []
sem_erro = []

for i in funcionario:
    try:
        #valida nome
        if len(i['nome']) == 0:
            com_erro.append(i)
        elif any(char.isdigit() for char in i['nome']):
            com_erro.append(i)

        #valida Area:
        elif i['area'] not in ('Vendas','TI','Financeiro','RH','Operações'):
            com_erro.append(i)

        #valida Salário:
        elif not isinstance(i['salario'], int):
            com_erro.append(i)
        elif i['salario'] < 0:
            com_erro.append(i)

        #valida bonus_percentual:
        elif len(i['bonus_percentual']) == 0:
            com_erro.append(i)
        elif not 0 <= float(i['bonus_percentual']) <= 1:
            com_erro.append(i)

        else:
            sem_erro.append(i)
    except ValueError:
        com_erro.append(i)

com_erro
