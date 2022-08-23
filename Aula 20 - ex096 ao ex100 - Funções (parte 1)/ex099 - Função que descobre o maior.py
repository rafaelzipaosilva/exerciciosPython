'''
Faça um programa que tenha uma função chamada maior(),
 que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'''
from time import sleep
def maior(* num):
    cont = maior = 0
    print('=-'* 30)
    print('Analisando os valores passados...')
    sleep(1)
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = 0
        else:
            maior = num[0]
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa principal
maior(3, 2, 4, 4)
maior()
maior(2, 6, 7)
maior(-2, -48)