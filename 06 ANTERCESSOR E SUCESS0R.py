"""
06)FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE SEU SUCESSOR E SEU ANTECESSOR !



"""
valor = int(input('DIGITE UM VALOR:'))

antecessor = valor - 1
sucessor = valor + 1

print('analisando o valor \033[0;33m{}\033[m, seu antecessor é \033[0;33m{}\033[m e o sucessor é \033[0;34m{}\033[m'
      .format(valor, antecessor, sucessor))

# OUTRA FORMA

''''valor=int(input('DIGITE UM NUMERO'))

print('analizando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(valor,(valor-1),(valor+1)))'''
