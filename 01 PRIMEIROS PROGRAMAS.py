"""
EX0: CRIE UM PROGRAMA QUE ESCREVA "OLÁ, MUNDO!" NA TELA

"""
print('OLA, MUNDO!')

print(">>>>" * 10)
"""
EX1: CRIE UM SCRIPT PYTHON QUE LEIA O NOME DE UMA PESSOA E MOSTRE UMA MENSAGEM DE BOAS-VINDAS DE ACORDO
CO O VALOR DIGITADO

"""

nome = (str(input('digite seu nome:'))).upper()

print('É UM PRAZER EM TE CONHERCER {}!'.format(nome))

print(">>>>" * 10)
"""
EX2: CRIE UM SCRIPT PYTHON QUE LEIA O DIA,O MÊS EO ANO DE NASCIMENTO DE UMA PESSOA E MOSTRE UMA MENSAGEM COM A DATA
FORMATADA

"""

dia = int(input("DIA:"))
mes = str(input("MES:"))
ano = int(input("ANO:"))

print("VOCE NASCEU NO DIA {} DE {} DE {}. CORRETO".format(dia, mes, ano))


print(">>>>" * 10)
"""
EX3: CRIE UM SCRIPT PYTHON QUE LEIA DOIS NÚMERO E MOSTRE A SOMA ENTRE ELES
"""

NUM1 = float(input("INFORME O PRIMEIRO NÚMERO:"))
NUM2 = float(input("INFORME O SEGUNDO NÚMERO:"))

C = NUM1 + NUM2

print("A SOMA DE {} + {} = {}".format(NUM1, NUM2, C))
