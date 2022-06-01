"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

"""

valor = float(input('qual preço do produto? R$'))

porcentagen = (valor * 5) / 100
desconto = valor - porcentagen

print('O PRODUTO QUE CUSTAVA R${} NA PROMOÇÃO COM DESCONTO DE 5% VAI CUSTAR R${:.2f}'.format(valor, desconto))
