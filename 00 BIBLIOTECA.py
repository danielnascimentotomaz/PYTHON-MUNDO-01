###########BIBLIOTECA DE rondon[aleátorio]##############

"""
### randon.choice ## escolher nome aleatorio na lista

a=str(input('digite seu nome'))
b=str(input('digite seu nome'))
c=str(input('digite seu nome'))
d=str(input('digite seu nome'))

lista=[a, b, c, d]

escolhido=random.choice(lista)

print('o aluno escolhido foi {}'.format(escolhido))"""

#######################################

"""### shuflle (baralhar)

lista=['daniel','saudade', 'amor', 'eterno']

random.shuffle(lista)

print(lista)"""
##########################################

"""### randon.randon() gera numero floatuante  aleatorio

a = random.random()
print(a)"""

###########################################
"""###randint (gera numero aleatorio no intervalo determinado

b=random.randint(1, 4)
print(b)"""
###############################################
"""## randrange(STOP) 
for c in range(1, 9):
    a=random.randrange(4)

print(a)"""
################################################

# SOTEAR UMA LISTA COM RANDINT
""""
import random

aleatório = random.randint(0, 2)

lista = ['daniel', 'saudade', 'amor'] # OBS: QUANTIDADE DE ITENS DA LISTA TEM QUE SER IGUAL TOTAL QUE O RANDINT VAI SOTEAR

valor = int(input('valor'))

mostrar = lista[aleatório]
mostrar1 = lista[valor]
print(mostrar)
print(mostrar1)
"""
##################################################

"""# SORTEAR UM LISTA DE NUMERO:

from random import sample
a = tuple(sample(range(20), 10)) ## OBS ## 20 É O INTERVALO ###### 10 É QUANTOS NUMEROS EU QUERO SORTEI
print(a)"""




##################################################

# ######## BIBLIOTECA TIME (tempo)################

"""
import time

tempo = time.asctime()# vai mostra mês ano e horario
print(tempo)

a = time.localtime()  # LISTA TEMPO

print(a[0])  # ANO
print(a[1])  # MÊS
print(a[2])  # DIA MÊS
print(a[3])  # HORAS
print(a[4])  # MINUTOS
print(a[5])  # SEGUNDOS
print(a[6])  # DIA DA SEMANA
print(a[7])  # DIA DA ANO
"""
##########################################
"""import time
print('processando....')  # espera um tempo pra processar
time.sleep(5)
"""
#############################################


############# CONTAR E ACUMULAR VALORES ##########

soma = 0
count = 0

for c in range(1, 5):
    soma = soma + c
    count = count + 1
print('A SOMA É IQUAL {}'.format(soma))
print('O TOTAL DE VALORES É {}'.format(count))