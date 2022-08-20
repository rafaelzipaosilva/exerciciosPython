# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua Porção Inteira.


#Importando a função trunc da biblioteca math
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a porção inteira é {}'.format(num, trunc(num)))

'''
# Usando a função interna int
    num = float(input('Digite um valor: '))
    print('O valor digitado foi {} e a porção inteira é {}'.format(num, int(num)))
'''