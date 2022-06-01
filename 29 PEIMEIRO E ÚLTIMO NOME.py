"""
29) Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
 primeiro e o último nome separadamente.

"""

nome = str(input('DIGITE SEU NOME COMPLETO:')).strip()
print('MUITO PRAZER EM TE CONHECER:')

dividir = nome.split()

comprimento = len(dividir)

print('SEU PRIMEIRO NOME É {}'.format(dividir[0]))

print('SEU ÚLTIMO NOME É {}'.format(dividir[comprimento - 1]))
