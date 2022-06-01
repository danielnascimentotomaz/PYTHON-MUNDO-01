# IMPORTE BIBLIOTECA:

''''
import => vai importa todas funcionalidades do módulo

EX:import math
vai importa toda funcionalidade de  matématica


from => vai importa apenas que eu desejar

EX:from maht import sqrrt

vai importa apenas a funcionalidade raiz quadrada
'''

## EX:UTILIZANDO import math####

import math

numero = float(input('digite um numero:'))

raiz = math.sqrt(numero)

print('VALOR DA RAIZ QUADRADA DE {} É {}'.format(numero, raiz))

## EX:UTILIZANDO from math import sqrt

from math import sqrt

numero = float(input('ditite um numero..'))

raiz = sqrt(numero)


print('VALOR DA RAIZ QUADRADA DE {} É {}'.format(numero, raiz))
