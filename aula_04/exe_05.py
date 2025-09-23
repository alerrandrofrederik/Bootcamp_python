import csv  # importa o módulo csv da biblioteca padrão do Python

resultados = []  # cria uma lista vazia para armazenar as linhas processadas

# Abre o arquivo vendas.csv para leitura
with open("aula_04/vendas.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)  # lê cada linha como dicionário (chave = nome da coluna)

    # percorre cada linha do arquivo
    for linha in leitor:
        quantidade = int(linha["quantidade"])  # converte quantidade de string para inteiro
        preco = float(linha["preco"])          # converte preço de string para float
        total = quantidade * preco             # calcula o valor total da venda

        linha["total"] = total                 # adiciona uma nova chave "total" na linha
        resultados.append(linha)               # guarda a linha modificada na lista resultados

# Abre um novo arquivo vendas_total.csv para escrita
with open("vendas_total.csv", mode="w", encoding="utf-8", newline="") as saida:
    nomes_colunas = resultados[0].keys()  # pega automaticamente os nomes das colunas a partir da primeira linha
    escritor = csv.DictWriter(saida, fieldnames=nomes_colunas)  # cria o escritor de CSV com cabeçalhos

    escritor.writeheader()       # escreve o cabeçalho no novo arquivo
    escritor.writerows(resultados)  # escreve todas as linhas processadas de uma vez
