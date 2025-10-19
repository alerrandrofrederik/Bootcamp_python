
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
            'salario':(linha['salario']),
            'bonus_percentual':(linha['bonus_percentual'])
        }
        for linha in leitor
    ]

funcionario
# %%
com_erro = []
sem_erro = []

for i in funcionario:
    #valida nome
    if len(i['nome']) == 0:
        com_erro.append(i)
    elif any(char.isdigit() for char in i['nome']):
        com_erro.append(i)
    #valida Area:
    elif i['area'] not in ('Vendas','TI','Financeiro','RH','Operações'):
        com_erro.append(i)
    else:
        sem_erro.append(i)

com_erro