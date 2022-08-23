# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

while True:
    lista.append(int(input(f'Digite um número: ')))
    r = str(input(f'Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
lista.sort()
for i, v in enumerate(lista):
    if v % 2:
        par.append(v)
    else:
        impar.append(v)

print('=-' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')
