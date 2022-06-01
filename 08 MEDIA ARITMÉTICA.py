"""
08)Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

"""


nota1 = float(input('PRIMEIRA NOTA DO ALUNO:'))
nota2 = float(input('SEGUNDA NOTA DO ALUNO:'))

media = (nota1+nota2)/2

print('A MEDIA ENTRE {:.1f} E {:.1f} É IQUAL A {:.1f}'.format(nota1, nota2, media))