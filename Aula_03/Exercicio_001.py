# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores 
# positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" 
# se ambos forem positivos ou "Dados inválidos" caso contrário.

quantidade = 10  # Exemplo de valor, substitua com input do usuário se necessário
preço = 20  # Exemplo de valor, substitua com input do usuário se necessário

if quantidade > 0 and preço > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")