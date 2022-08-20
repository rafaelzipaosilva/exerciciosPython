# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro),
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
c50 = c20 = c10 = c1 = 0
while True:
    n = float(input('Qual valor que deseja sacar: R$ '))
    t = n
    if n <= 0:
        break
    else:
        c50 = int(n // 50)
        n -= c50 * 50
        if n >= 20:
            c20 = int(n // 20)
            n -= c20 * 20
        if n >= 10:
            c10 = int(n // 10)
            n -= c10 * 10
        if n >= 1:
            c1 = int(n // 1)
        break
if n <= 0:
    print('O valor solicitado é inválido. PROGRAMA ENCERRADO.')
else:
    print(f'Valor solicitado: R$ {t:.2f}')
    if c50 != 0:
        print(f'{c50} cédulas de R$ 50,00')
    if c20 != 0:
        print(f'{c20} cédulas de R$ 20,00')
    if c10 != 0:
        print(f'{c10} cédulas de R$ 10,00')
    if c1 != 0:
        print(f'{c1} cédulas de R$ 1,00')
    print('Programa encerrado. Volte sempre!')
# print(f'{n} total\n{c50} nota 50\n{c20} nota 20\n{c10} nota 10\n{c1} nota 1')
