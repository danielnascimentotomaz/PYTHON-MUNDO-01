"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

"""

import random

lista = []

a = lista.append(str(input('PRIMERO ALUNO:')))
b = lista.append(str(input('SEGUNDO ALUNO:')))
c = lista.append(str(input('TERCEIRO ALUNO:')))
d = lista.append(str(input('QUARTO ALUNO:')))

escolhido = random.choice(lista)  # choice.. vai escolher um  dentro de uma lista

print('O ALUNO ESCOLHIDO FOI {} '.format(escolhido))

