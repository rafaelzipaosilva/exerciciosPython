# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('\033[34m1º número:\033[m '))
n2 = int(input('\033[35m2º número:\033[m '))
menu = 0
r = 0
while menu != 5:
    menu = int(input('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    >>>>> Qual é a sua opção? '''))
    if menu == 1:
        r = n1 + n2
        print('A SOMA\033[m dos números \033[34m{}\033[m e \033[35m{}\033[m é igual a \033[32m{}\033[m.'.format(n1, n2, r))
    elif menu == 2:
        r = n1 * n2
        print('O PRODUTO\033[m dos números \033[34m{}\033[m e \033[35m{}\033[m é igual a \033[32m{}\033[m.'.format(n1, n2, r))
    elif menu == 3:
        if n1 > n2:
            print('O maior número\033[m digitado é o \033[34m{}\033[m.'.format(n1))
        elif n1 < n2:
            print('O maior número\033[m digitado é o \033[35m{}\033[m.'.format(n2))
        else:
            print('Os dois números digitados são \033[32miguais\033[m')
    elif menu == 4:
        print('Digite novos números: ')
        n1 = int(input('\033[34m1º número:\033[m '))
        n2 = int(input('\033[35m2º número:\033[m '))
    elif menu == 5:
        menu = 5
    else:
        print('\033[1:31mOpção incorreta! Tente novamente!\033[m')
    print('-=' * 15)
    sleep(2)
print('Muito obrigado por usar este programa')