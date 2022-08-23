'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
grupo = []
pessoa = []
pmaior = pmenor = 0
#
while True:
    pessoa.append(str(input('Digite o nome da pessoa: ')))
    pessoa.append(float(input('Digite o peso: ')))
    if len(grupo) == 0:
        pmaior = pmenor = pessoa[1]
    else:
        if pessoa[1] > pmaior:
            pmaior = pessoa[1]
        if pessoa[1] < pmenor:
            pmenor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
#
print('=-' * 30)
print(f'Número de cadastros: {len(grupo)} pessoas.')
#
print(f'O maior peso registrado foi {pmaior} para as pessoas: ', end='')
for p in grupo:
    if p[1] == pmaior:
        print(f'[{p[0]}] ', end='')
print()
#
print(f'O menor peso registrado foi {pmenor} para as pessoas: ', end='')
for p in grupo:
    if p[1] == pmenor:
        print(f'[{p[0]}] ', end='')
