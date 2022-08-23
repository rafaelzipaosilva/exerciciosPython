# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
termos = int(input('Quantos termos da Sequência de Fibonacci você quer ver? '))
print('-='*5, 'SEQUÊNCIA DE FIBONACCI', '-='*5)
cont = 0
n1 = 0
n2 = 1
n3 = 1
while cont < termos:
    print(n1, end=' - ')
    cont += 1
    n1 = n2
    n2 = n3
    n3 = n1 + n2
print('FIM')




