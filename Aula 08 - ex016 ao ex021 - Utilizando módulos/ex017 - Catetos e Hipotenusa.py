# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# utilizando biblioteca

from math import hypot
ca = float(input('Comprimento do cateto adjacente: '))
co = float(input('Comprimento do cateto oposto: '))

print('O valor da hipotenusa é {:.2f}'.format(hypot(ca, co)))

'''
# utilizando conceitos matemáticos
    ca = float(input('Comprimento do cateto adjacente: '))
    co = float(input('Comprimento do cateto oposto: '))
    hip = (ca ** 2 + co ** 2) ** (1/2)

    print('O valor da hipotenusa é {:.2f}'.format(hip))
'''