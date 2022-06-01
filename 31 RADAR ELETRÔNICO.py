"""
31)Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

"""

velocidade = float(input('QUAL É A VELOCIDADE ATUAL DO CARRO!'))

if velocidade > 80:
    multa = (velocidade-80) * 7
    print("""\n\033[31mMULTADO! VOCÊ EXCEDEU O LIMITE PERMITIDO QUE É DE 80KM/h  
VOCÊ DEVE PAGAR UMA MULTA DE\033[m\033[33m R${:.2f}!\033[m """.format(multa))


print('\n\033[32mTENHA BOM DIA! DIRIJA COM SEGURANÇA!\033[m')
