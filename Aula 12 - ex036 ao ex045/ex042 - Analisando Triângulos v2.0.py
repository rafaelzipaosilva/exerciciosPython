# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segunda segmento: '))
l3 = float(input('Terceira segmento: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Os três segmentos FORMAM um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os três segmentos não formam um triângulo!')

''' OUTRA RESOLUÇÃO DO EXERCÍCIO
if l1 != l2 and l2 != l3 and l3 != l1:
    print('É um TRIÂNGULO ESCALENO')
elif l1 == l2 and l2 == l3 and l3 == l1:
    print('É um TRIÂNGULO EQUILÁTERO')
elif l1 == l2 or l2 == l3 or l3 == l1:
    print('É um TRIANGULO ISÓSCELES')
'''
