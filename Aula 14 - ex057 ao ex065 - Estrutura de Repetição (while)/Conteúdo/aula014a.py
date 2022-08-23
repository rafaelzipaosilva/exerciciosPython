'''for c in range(1,10):
    print(c)
print('FIM')''' #controle versão for

'''
c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print('FIM')''' # ccontrole versão while

'''
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
''' # controle de caixa zerada

'''
r = 'S'
while r != 'N':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N]: ')).upper()
print('FIM')
''' # controle de continuidade

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))