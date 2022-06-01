"""
09)Escreva um programa que leia um valor em metros e o exiba convertido em kilometro, hectômetro,
decâmetro, decimetro, centímetros e milímetros.

"""


metro = float(input('DIGITE UM VALOR EM METRO:'))

KM = metro / 1000
HAM = metro / 100
DAM = metro / 10
DM = metro * 10
CM = metro * 100
MM = metro * 1000

print('A MEDIDA DE {} METROS CORRESPONDE A'.format(metro))

print('{}KM'.format(KM))
print('{}HAM'.format(HAM))
print('{}DAM'.format(DAM))
print('{:.0f}DM'.format(DM))
print('{:.0f}CM'.format(CM))
print('{:.0f}MM'.format(MM))

'''   #########           OUTRA FORMA    ###########

metro=float(input('digite um distância em mtros:'))

print('A MEDIDA DE {} METROS CORRESPONDE A'.format(metro))
print('{}KM'.format((metro/1000)))
print('{}HAM'.format((metro/100)))
print('{}DAM'.format((metro/10)))
print('{:.0f}DM'.format((metro*10)))
print('{:.0f}CM'.format((metro*100)))
print('{:.0f}MM'.format((metro*1000)))'''
