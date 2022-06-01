"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
ela pode comprar.

conseidere U$$1.00 =R$3.27
"""

moeda = float(input('QUANTOS DINHEIRO VOCÊ TEM NA CARTEIRA? R$'))

total = moeda / 3.27

print('COM R${} VOCÊ PODE COMPRAR UU${:.2f}'.format(moeda, total))
