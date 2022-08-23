'''
Faça um programa que tenha uma função chamada área(),
 que receba as dimensões de um terreno retangular (largura e comprimento)
 e mostre a área do terreno.
'''
def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {area:.1f}m².')


#Programa principal
print('<< Controle de Terreno >>')
print('-' * 30)
l = float(input(f'LARGURA (m): '))
c = float(input(f'COMPRIMENTO (m): '))
area(l, c)
