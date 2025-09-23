
# %%
# 4. fassa um programa que peça dois numeros inteiros a divisão inteira do primeiro pelo segundo 

primeiro_numero = int(input("digite o primeiro número: "))
segundo_numero = int(input("digite o segundo número: "))

divisao = primeiro_numero // segundo_numero

print('A divisão de ',primeiro_numero," por ",segundo_numero, " é igual a: ",  divisao)

# %%
#15. Escreva um programa que peça ao usuário uma data no formato "dd/mm/aaaa", em seguida imprima dia mês e ano.

## trabalhando dom date time
from datetime import datetime, date, time, timedelta

current_datetime = datetime.now()
print(f"Current datetime: {current_datetime}")

print(current_datetime.day)
print(current_datetime.month)
print(current_datetime.year)
# %%
## trabalhando com dado no formato string
data = '21/09/2025'
data = data.split('/')
data[0]

# %%
