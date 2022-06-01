### MANIPULANDO CADEIA DE TEXTO


################ FATIAMENTO ###########################

frase = 'curso em video python'

# ex1: PEGA UMA LETRA DENTRO DA FRASE  [x]
print(frase[9])

# EX2: COMECAR DE UMA LETRA ATÉ ONDE DESEJA [x:y]
# OBS: VAI CONTA ATÉ A LETRA 12 PORQUE O ULTIMO VALOR NÃO ENTRA NA CONTA
print(frase[9:13])

# EX3: PULAR LETRA [x:y:z]
print(frase[9:21:2])

# EX3: VAI COMECAR DO COMEÇO E VAI ATÉ A LETRA PRETENDIDA [:x]

print(frase[:5])

# X4 COMECA APARTIR DO NUMERO SELECIONADO ATÉ  O FINAL [x:]

print(frase[15:])

# EX5:VAI COMEÇA DO X ATÉ O FINAL PULANDO EM V EM V [x::v]

print(frase[9::3])

#################  ANÁLISE   ##################

# len=comrimento
# count=contar
# find encontrar (rfind pela direita......)
# in = existir

print(len(frase))
print(frase.count('o'))
print(frase.count('o', 1, 13))  # COM FATIAMENTO
print(frase.find('video'))  # vai mostra da onde comeca a frase
print(frase.find('android'))  # QUANDO COLOCAR UM NOME QUE NÃO EXISTIR MIM RETORNA -1 ( NÃO FOI ENCONTRADO)
print('video' in frase)  # retorna  um valor verdadeiro ou falso

################### TRANSFORMAÇÃO ##########################

# replace = substituir
# upper  = maiuscula
# lower = minuscula
# capitalize = transformar primeira letra da frase pra maiuscula
# title = vai transformar todas palavra da frase a primeira letra pra maiuscula
# strip = vai remover espaço  no inicio e final da frases...(rstrip vai remover da direita,  lstrip vai remover da esquerda)

print(frase.replace('python', 'java'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())

########################## DIVISÃO #########################

# split = vai dividir onde frase tiver espaco e criar uma lista
print(frase.split())

###########  JUNCÃO ##################
# ''.join

print(''.join(frase))

#### ESCRREER UM TEXTO GRANDE TELA


print("""aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
cccccccccccccccccccccccccccccccc""")

###################  FATIAMENTO DE NUMERO ###################
numero = 4456

u = numero // 1
d = numero // 10
c = numero // 100
m = numero // 1000

u1 = u % 10  ## SE AUMENTA PRA 100 VAI APARECER DUAS CASAS DECIMAIS, 1000 TRES CASAS DECIMAIS ASSIM DIANTE
d1 = d % 10
c1 = c % 10
m1 = m % 10

print(u, u1)
print(d, d1)
print(c, c1)
print(m, m1)
