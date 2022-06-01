"""
 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
 e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma
  área de 2 metros quadrado

"""

largura = float(input('largura  da parede:'))
altura = float(input('altura da parede:'))

area = largura * altura

quantidade = area / 2

print('sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(largura, altura, area))
print('para pinta essa parede ,você precisará de {:.2f} litro de tintas'.format(quantidade))
