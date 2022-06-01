"""
35) Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

valor1 = int(input('PRIMEIRO VALOR:'))
valor2 = int(input('SEGUNDO VALOR: '))
valor3 = int(input('DIGITE TERCEIRO VALOR:'))

# verificando maior valor

maior = valor1

if valor2 > valor1 and valor2 > valor3:
    maior = valor2

if valor3 > valor1 and valor3 > valor1:
    maior = valor3

print('O MAIOR VALOR DIGITADO FOI \033[33m{}\033[m'.format(maior))

# verificando menor valor


menor = valor1

if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor2 and valor3 < valor1:
    menor = valor3

print('O MENOR VALOR DIGITADO FOI \033[31m{}\033[m'.format(menor))
