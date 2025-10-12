
import csv

sem_erro = []
com_erro = []

with open("desafio_01/funcionarios.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        nome = linha["nome"].strip()
        area = linha["area"].strip()
        salario = linha["salario"].strip()
        bonus_percentual = linha["bonus_percentual"].strip()

        # validação do nome
        if len(nome) == 0:
            linha['check_nome'] = 'Nome vazio'
            com_erro.append(linha)
        elif any(char.isdigit() for char in nome):
            linha['check_nome'] = 'Nome não pode conter números'
            com_erro.append(linha)

        # validação do area
        elif area not in ('Vendas','TI','Financeiro','RH','Operações'):
            linha['check_area'] = 'area invalida'
            com_erro.append(linha)

        # # validação do Salário
        try:
            valor = int(salario)
            if valor < 0:
                linha['check_salario'] = "Salário não pode ser negativo"
                com_erro.append(linha)
        except ValueError:
            linha['check_salario'] = "Salário deve ser do tipo inteiro"
            com_erro.append(linha)

        # # validação do bonus_percentual
        # try:
        #     valor = float(bonus_percentual)
        # except ValueError:
        #     linha['check_bonus_percentual'] = 'bonus_percentual deve ser do tipo float'
        #     com_erro.append(linha)

        # if len(bonus_percentual) == 0:
        #     linha['check_bonus_percentual'] = 'bonus_percentual vazio'
        #     com_erro.append(linha)

        # if not (0 <= valor <= 1):
        #     linha['check_bonus_percentual'] = 'bonus_percentual deve ser entre 0 e 1 (inclusive)'
        #     com_erro.append(linha)

        else:
            sem_erro.append(linha)

print("Sem erro:", sem_erro)
print("Com erro:", com_erro)