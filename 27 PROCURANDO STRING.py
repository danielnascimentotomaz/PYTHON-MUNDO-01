"""
27) Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

"""

nome = str(input('QUAL SEU NOME COMPLETO:')).strip().upper()

achar = 'SILVA' in nome

print('SEU NOME TEM SILVA?{}'.format(achar))
