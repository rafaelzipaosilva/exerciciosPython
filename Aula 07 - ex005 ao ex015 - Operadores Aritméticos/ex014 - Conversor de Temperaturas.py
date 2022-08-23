# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em ºC: '))
f = (c * 9/5) + 32
k = c + 273.15

print('A temperatura de {:.2f}ºC equivale a {:.2f}ºF e a {:.2f}K'.format(c, f, k))
