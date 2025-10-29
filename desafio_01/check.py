
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
            sem_erro.append(i)
    except ValueError:
        i['erro'] = 'valor invalido check os valores'
        com_erro.append(i)

com_erro
# %%
#  registros inválidos com o motivo do erro em csv

with open('erros.csv', mode='w', encoding='utf-8', newline='') as file:
    nomes_colunas = com_erro[0].keys()
    escritor = csv.DictWriter(file, fieldnames=nomes_colunas)

    escritor.writeheader()
    escritor.writerows(com_erro)

# %%
