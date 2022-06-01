"""
17)Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

"""

import math

valor = float(input('digite um valor:'))

total = math.trunc(valor)

print('O VALOR DIGITADO FOI {} E SUA PORÇÃO INTEIRA É {}'.format(valor, total))


"""#### OUTRA FORMA(importando apenas a funcão trunc)

from math import trunc

valor = float(input('digite um valor'))

total=trunc(valor)

print('O VALOR DIGITADO FOI {} E SUA PORCÃO INTEIRA É {}'.format(valor, total))"""