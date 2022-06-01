"""
25) Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

from time import sleep

numero = int(input('informe um número'))

print('ANALISANDO O NÚMERO {}'.format(numero))
sleep(2)

unidade = numero // 1
dezena = numero // 10
centena = numero // 100
milhar = numero // 1000

print('UNIDADE:{}'.format(unidade % 10))
print('DEZENA:{}'.format(dezena % 10))
print('CENTENA:{}'.format(centena % 10))
print('MILHAR: {}'.format(milhar % 10))

# obs : o resto da divisão por 10 mim retorna o último número

"""#### PODIA SER FEITO DESSA FORMA MAIS DA ERRO SE DIGITAR MENOS 4 ALGARISMO

numero=str(input('informe um numero:'))

unidade=str(numero[3])
dezenas=str(numero[2])
centenas=str(numero[1])
milhar=str(numero[0])

print('analisando o número {}'.format(numero))

print('UNIDADE:{}'.format(unidade))
print('DEZENA:{}'.format(dezenas))
print('CENTENA:{}'.format(centenas))
print('MILHAR:{}'.format(milhar))"""
