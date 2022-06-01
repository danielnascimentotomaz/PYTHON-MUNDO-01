"""
24) Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.


"""

from time import sleep

nome = str(input('DIGITE SEU NOME COMPLETO:')).strip()

print('ANALIZANDO SEU NOME.....')
sleep(2)

dividir = nome.split()

contar = ''.join(dividir)

print('SEU NOME EM MAIUSCULAS É \033[31m{}\033[m'.format(nome.upper()))
print('SEU NOME EM MINUSCULA É \033[32m{}\033[m'.format(nome.lower()))
print('SEU NOME TEM AO TODO \033[33m{}\033[m LETRA'.format(len(contar)))
print('SEU PRIMEIRO NOME É \033[34m{}\033[m E ELE TEM \033[32m{}\033[m LETRA'.format(dividir[0], len(dividir[0])))
