# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segunda segmento: '))
l3 = float(input('Terceira segmento: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Os três segmentos formam um triângulo!')
else:
    print('Os três segmentos não formam um triângulo!')
