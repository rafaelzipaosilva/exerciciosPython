# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
b = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = b * h
t = a / 2

print('Sua parede tem a dimensão de {}mx{}m e sua area é de {:.2f}m²'.format(b, h, a))
print('Você vai precisar de {:.2f}l de tinta para pintar a parede'.format(t))