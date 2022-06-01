"""
26)Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

"""

cidade = str(input('EM QUE CIDADE VOÇÊ NASCEU:')).strip().upper()

dividir = cidade.split()

fatiamento = dividir[0]

print('SANTO' in fatiamento)  # ou print("{}".format(fatiamento == SANTO)


'''############  OUTRA FORMA #############

cidade = str(input('EM QUAL CIDADE VOÇÊ NASCEU')).strip()

resultado=cidade[:5] == 'SANTO'

print(resultado)'''
