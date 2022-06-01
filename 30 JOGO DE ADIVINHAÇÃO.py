"""
30)Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""

from time import sleep
from random import randint

print('\033[36m=--=\033[m' * 40)
print('\033[32mVOU PENSAR EM UM NÚMERO ENTRE 0 E 5.TENTE ADIVINHAR...\033[m')
print('\033[36m=--=\033[m' * 40)

numero = int(input('EM QUE NÚMERO EU PENSEI! '))

print('\033[34mprocessando...\033[m')
sleep(2)

# computador sorteando de 0 a 5
aleatorio = randint(0, 5)

if aleatorio != numero:
    print('\033[31mGANHEI! EU PENSEI NO {} E NÃO NO {}\033[m'.format(aleatorio, numero))

else:
    print('\033[35mPARABÉNS! VOCÊ CONSEQUIU MIM VENCER!\033[m')
