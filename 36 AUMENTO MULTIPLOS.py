"""
36) Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

"""

salario = float(input('QUAL É SALARIO DO FUNCIONARIO? R$'))

# aumento de 15%
if salario <= 1250:
    aumento = (salario * 15 / 100) + salario

# aumento de 10%
else:
    aumento = (salario * 10 / 100) + salario

print('QUEM GANHAVA R$\033[34m{:.2f}\033[m PASSA A GANHAR R$\033[32m{:.2f}\033[m AGORA'.format(salario, aumento))
