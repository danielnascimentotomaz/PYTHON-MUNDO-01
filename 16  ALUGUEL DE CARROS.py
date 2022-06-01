"""
16)Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
 e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
  o carro custa R$60 por dia e R$0,15 por Km rodado.

"""

dias = float(input('QUANTOS DIAS ALUGADOS?'))
rodados = float(input('QUANTOS KM RODADOS?'))

paga = (rodados * 0.15) + (dias * 60)

print('TOTAL A PAGAR É DE R$:\033[0;31m{:.2f}\033[m'.format(paga))
