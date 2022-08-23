# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
x = float(input('Digite o valor do ângulo: '))
sn = sin(radians(x))
print('O ângulo de {}º tem o valor do SENO de {:.2f}'.format(x, sn))
cs = cos(radians(x))
print('O ângulo de {}º tem o valor do COSSENO de {:.2f}'.format(x, cs))
tg = tan(radians(x))
print('O ângulo de {}º tem o valor da TANGENTE de {:.2f}'.format(x, tg))