# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# utilizando o formato de lista
lista = sorted([a, b, c])
print('O menor número é o {}'.format(lista[0]))
print('O maior número é o {}'.format(lista[2]))

#v erificando quem é o menor
'''menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor =c'''

# verificando quem é o maior
'''maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))'''