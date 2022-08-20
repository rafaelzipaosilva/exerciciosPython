# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
pri = int(input('1º termo: '))
r = int(input('Razão: '))
cont = 0
while cont < 10:
    print(pri, '¬ ', end='')
    pri += r
    cont += 1
print('ACABOU!')