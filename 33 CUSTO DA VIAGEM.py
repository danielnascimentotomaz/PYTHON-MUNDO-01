"""
33) Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
 cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.




"""

distancia = float(input('QUAL É A DISTÂNCIA DA SUA VIAGEM!'))

print('VOÇÊ ESTÁ PRESTE A COMECAR UMA VIAGEM DE {:.1f}KM'.format(distancia))

if distancia <= 200:
    valor1 = distancia * 0.50
    print('E O PREÇO DA SUA PASSAGEM SERÁ DE R${:.2f}'.format(valor1))

else:
    valor2 = distancia * 0.45
    print('E O PREÇO DA SUA PASSAGEM SERÁ DE R${:.2f}'.format(valor2))
