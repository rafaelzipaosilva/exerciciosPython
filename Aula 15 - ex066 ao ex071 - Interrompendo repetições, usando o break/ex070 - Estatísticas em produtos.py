# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
#   A) qual é o total gasto na compra.
#   B) quantos produtos custam mais de R$1000.
#   C) qual é o nome do produto mais barato.
barato = ctotal = cmil = 0
produto = pbarato = continuar = ' '
while True:
    produto = str(input('Produto: ')).upper().strip()
    valor = float(input('Valor: '))
    ctotal += valor
    if valor >= 1000:
        cmil += 1
    if barato == 0 or valor <= barato:
        barato = valor
        pbarato = produto
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto foi R$ {ctotal:.2f}.')
print(f'{cmil} produtos custam mais de R$ 1000,00.')
print(f'Produto mais barato: {pbarato}.')
print('-'*40)
