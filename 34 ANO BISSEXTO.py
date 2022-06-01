"""
34)Faça um programa que leia um ano qualquer e mostre se ele é bissexto.


"""

from datetime import date

ano = int(input('QUE ANO QUER ANALISAR! COLOQUE 0 PARA ANALISAR O ANO ATUAL:'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ANO {} É BISSEXTO'.format(ano))

else:
    print('O ANO {} NAO É BISSEXTO'.format(ano))
