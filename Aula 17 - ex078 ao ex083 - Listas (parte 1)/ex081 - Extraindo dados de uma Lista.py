# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    n = int(input(f'Digite um número: '))
    lista.append(n)
    print('Valor adiconado com sucesso!')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break

print('=-' * 32)
print(f'Foram digitados {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'A lista de valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O número 5 faz parte da lista!')
else:
    print(f'O número 5 não foi encontrado na lista!')
