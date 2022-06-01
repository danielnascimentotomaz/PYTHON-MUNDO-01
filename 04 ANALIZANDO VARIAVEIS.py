"""
Ex: FAÇA UM PROGRAMA QUE LEIA  ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO
E TODOS AS INFORMAÇÕES POSSIVEIS SOBRE ELE.




"""

coisa = (input('DIGITE ALGO!'))

print('seu tipo  primitivo desse valor é {}'.format(type(coisa)))
print('SÓ TEM ESPAÇO! {}'.format(coisa.isspace()))
print('É UM NÚMERO! {}'.format(coisa.isnumeric()))
print('É UM ALFABÉTICO! {}'.format(coisa.isalpha()))
print('É UM ALFANÚMERICO! {}'.format(coisa.isalnum()))
print('ESTÁ EM MAIÚSCULAS! {}'.format(coisa.isupper()))
print('ESTÁ EM MINÚCULAS! {}'.format(coisa.islower()))
print('ÉSTA CAPITALIZADA! {}'.format(coisa.istitle()))

# CAPITALIZADO É QUANDO COMEÇA COM LETRA MAIÚSCULA
