"""
32)Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

numero = int(input('\033[34mME DIGA UM NÚMERO QUALQUER:\033[m'))

if numero % 2 == 0:
    print('O NÚUMERO {} É \033[31mPAR\033[m'.format(numero))
else:
    print('O NÚMERO {} É\033[32m IMPAR\033[m'.format(numero))
