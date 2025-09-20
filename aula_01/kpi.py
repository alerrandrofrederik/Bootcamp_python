# %%
CONSTANTE_BONUS = 1000

nome_usuario = input("Digite um nome: ")
salario_usuario = float(input("Digite seu salário: "))
bonus_usuario =float(input("Digite seu bonus: "))

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

print(f"O valor do bonus de {nome_usuario} é {valor_do_bonus}")