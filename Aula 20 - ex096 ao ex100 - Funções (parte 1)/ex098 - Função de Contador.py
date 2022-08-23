'''
Faça um programa que tenha uma função chamada contador(),
 que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep

#defs
def mensagem(msg):
    tam = len(msg) + 4
    print(f'~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)

def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(1)
    if i < f:
        while i <= f:
            print(f'{i} ', end='', flush=True)
            sleep(0.5)
            i += p
        print('FIM!')
    elif i > f:
        while i >= f:
            print(f'{i} ', end='', flush=True)
            sleep(0.5)
            i -= p
        print('FIM!')
    print('-' * 30)

#Programa Principal
mensagem('FUNÇÃO DE CONTADOR')
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input(f'{"Início:":<10}'))
fim = int(input(f'{"Final:":<10}'))
pas = int(input(f'{"Passo:":<10}'))
contador(ini, fim, pas)
