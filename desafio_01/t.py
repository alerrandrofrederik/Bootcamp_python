import csv

def validar_nome(nome):
    if not nome:
        return "Nome vazio"
    if any(char.isdigit() for char in nome):
        return "Nome não pode conter números"
    return None

def validar_area(area):
    areas_validas = {"Vendas", "TI", "Financeiro", "RH", "Operações"}
    if not area:
        return "Área vazia"
    if area not in areas_validas:
        return "Área inválida"
    return None

def validar_salario(salario):
    if not salario:
        return "Salário vazio"
    try:
        valor = int(salario)
        if valor < 0:
            return "Salário não pode ser negativo"
    except ValueError:
        return "Salário deve ser do tipo inteiro"
    return None

def validar_bonus(bonus):
    if not bonus:
        return "Bonus percentual vazio"
    try:
        valor = float(bonus)
        if not (0 <= valor <= 1):
            return "Bonus percentual deve estar entre 0 e 1 (inclusive)"
    except ValueError:
        return "Bonus percentual deve ser do tipo float"
    return None


sem_erro = []
com_erro = []

with open("desafio_01/funcionarios.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        erros = {}

        # validações
        if erro := validar_nome(linha["nome"].strip()):
            erros["check_nome"] = erro

        if erro := validar_area(linha["area"].strip()):
            erros["check_area"] = erro

        if erro := validar_salario(linha["salario"].strip()):
            erros["check_salario"] = erro

        if erro := validar_bonus(linha["bonus_percentual"].strip()):
            erros["check_bonus_percentual"] = erro

        if erros:
            linha.update(erros)
            com_erro.append(linha)
        else:
            sem_erro.append(linha)

print("Sem erro:", sem_erro)
print("Com erro:", com_erro)
