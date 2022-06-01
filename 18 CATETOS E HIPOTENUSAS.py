"""
18) Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
 de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

"""

import math

co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente: '))

hi = math.hypot(co, ca)

print('A HIPOTENUSA AI MEDIR {:.2f}'.format(hi))

"""  #  OUTRA FORMA

co=float(input('comprimento do cateto oposto:'))
ca=float(input('comprimento do cateto adjacente:'))
total= ((ca ** 2 )+ (co ** 2))**(1/2)

print('A HIPOTENUSA VAI MEDIR {:.2f}'.format(total))"""
