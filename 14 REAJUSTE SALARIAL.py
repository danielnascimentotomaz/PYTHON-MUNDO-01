"""
14)Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

"""

salario = float(input('QUAL SALARIO DO FUNCIONÁRIO R$'))

porcentagen = (salario * 15) / 100

reajuste = porcentagen + salario

print('UM FUNCIONÁRIO QUE GANHAVA R${:.2f}, COM 15% DE AUMENTO PASSA RECEBER R${:.2f}'.format(salario, reajuste))
