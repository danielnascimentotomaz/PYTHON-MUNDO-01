"""
28)Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
aparece a primeira vez e em que posição ela aparece a última vez.

"""

frase = str(input('DIGITE UMA FRASE:')).strip().upper()

contar = frase.count('A')

encontra = frase.find('A')

encontra1 = frase.rfind('A')

print('a letra A aparece {} vezes na frase'.format(contar))

print('a letra A apareceu na posicão {}'.format(encontra + 1))

print('a última letra A apareceu na posicão {}'.format(encontra1 + 1))
