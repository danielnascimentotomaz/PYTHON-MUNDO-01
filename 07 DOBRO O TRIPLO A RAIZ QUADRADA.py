"""
07) Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

"""

valor = float(input('DIGITE UM NUMERO:'))

dobro = valor * 2

triplo = valor * 3

raiz = valor ** (1 / 2)

print('O DOBRO DE {} VALE {}'.format(valor, dobro))
print('O TRIPLO DE {} VALE {}'.format(valor, triplo))
print('A RAIZ QUADRADA DE {} É IQUAL A {:.2f}'.format(valor, raiz))

'''         ### OUTRA FORMA###

valor=float(input('DIGITE UM NUMERO'))

print('O DOBRO DE {} VALE {}'.format(valor,(valor*3)))
print('O TRIPLO DE {} VALE {}'.format(valor,(valor*3)))
print('A RAIZ QUADRADA DE {} É IQUAL A {:.2f}'.format(valor,(valor**(1/2))))'''
