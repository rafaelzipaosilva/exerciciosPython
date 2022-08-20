#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário,
# 2 para octal e
# 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))
escolha = int(input('''Para qual base você quer converter esse número?
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
Sua opção: '''))

print('')
print('\033[7;36m-*\033[m' * 20)
if escolha == 1:
    print('Você digitou o número \033[4;33m{}\033[m'.format(numero))
    print('Base binária: {0:b}'.format(numero))
elif escolha == 2:
    print('Você digitou o número \033[4;34m{}\033[m'.format(numero))
    print('Base octal: {0:o}'.format(numero))
elif escolha == 3:
    print('Você digitou o número \033[4;35m{}\033[m'.format(numero))
    print('Base hexadecimal: {0:x}'.format(numero))
else:
    print('\033[1:31mOPÇÃO INVÁLIDA!!!\033[m Por favor, tente novamente.')
print('\033[7;36m-*\033[m' * 20)