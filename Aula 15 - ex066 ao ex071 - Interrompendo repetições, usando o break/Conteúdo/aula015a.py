'''
cont = 1
while cont <=:
    print(cont, '->  ', end='')
    cont += 1
print('Acabou')
'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}') #usando F string

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e recebe R${salario:.2f}')