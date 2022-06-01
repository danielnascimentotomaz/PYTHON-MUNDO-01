"""
19)Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.

"""

"""import math

angulo=float(input('DIGITE O ÂNGULO QUE DESEJA:'))

seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))

print('o ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('o ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('o ângulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))"""

#####   OUTRA FORMA  ######

from math import radians, cos, sin, tan

valor = float(input('QUAL O ÂNGULO!'))

seno = sin(radians(valor))
cosseno = cos(radians(valor))
tangente = tan(radians(valor))

print('O ÂNGULO DE {} TEM O SENO DE {:.2f}°'.format(valor, seno))
print('O ÂNGULO DE {} TEM O COSSENO DE {:.2f}°'.format(valor, cosseno))
print('O ÂNGULO DE {} TEM A TANGENTE DE {:.2f}°'.format(valor, tangente))
