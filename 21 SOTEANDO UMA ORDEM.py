"""
21)O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

"""

import random

lista = []
a = lista.append(str(input('primeiro nome:')))
b = lista.append(str(input('segundo nome:')))
c = lista.append(str(input('terceiro nome:')))
d = lista.append(str(input('quarto nome:')))

random.shuffle(lista)  # shuffle vai barralar

print('A ORDEM DE APRESENTAÇÃO SERÁ ')
print(lista)