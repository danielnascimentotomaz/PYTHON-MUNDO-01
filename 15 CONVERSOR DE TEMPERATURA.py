"""
15)Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit e kelvin.

"""

temperatura = float(input('informe a temperatura em °C:'))

fahrenheit = (temperatura * 9 / 5) + 32
kelvin = temperatura + 273

print('A TEMPERATURA DE {}°C CORRESPONDE A {:.2f}°F'.format(temperatura, fahrenheit))
print('A TEMPERATURA DE {}°C CORRESPONDE A {:.2f}°K'.format(temperatura, kelvin))
