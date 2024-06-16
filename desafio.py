# Digitar o nome
nome = input("Digite seu nome: ")
# Digitar salário
salario = float(input("Digite seu salário: "))
# Digitar percentual do bônus
perc_bonus = float(input("Digite seu precentual de bônus: "))
# Calculo
bonus = 1000+salario*perc_bonus

#Resultado
print(f"Olá {nome}, seu bônus de 2024 é de {bonus}")