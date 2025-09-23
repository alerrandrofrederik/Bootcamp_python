
import csv

caminho_arquivo = "aula_04/usarios.csv"

with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha["nome"], linha["idade"])
