print('=-=' * 20)
print('ANALISADOR DE TRIÂNGULO')
print('=-=' * 20)

a = float(input('PRIMEIRO SEGMENTO'))
b = float(input('SEGUNDO SEGMENTO'))
c = float(input('TERCEIRO SEGMENTO'))

if a < (b + c) and b < (a + c) and c < (b + a):
    print('\033[33mOS SEGMENTO ACIMA PODEM FORMAR TRIÂNGULO\033[m')
else:
    print('\033[31mOS SEGMENTO ACIMA NÃO PODEM FORNAR TRIÂNGULO\033[31m')


"""
a = float(input("PRIMEIRO SEGMENTO: "))
b = float(input("SEGUNDO SEGMENTO: "))
c = float(input("TERCEIRO SEGMENTO: "))

maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

if (a + b + c - maior) > maior:
    print("OS SEQMENTO PODE FORMAR UM TRIÂNGULO")
else:
    print("NÃO PODE FORMA UM TRIÂMGULO")






"""