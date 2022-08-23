# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
cont = 0
print('-='*20)
print('JOGO DE PAR OU ÍMPAR')
while True:
    print('-=' * 20)
    pessoa = int(input('Digite um número: '))
    pc = randint(1, 10)
    soma = pessoa + pc
    res = soma % 2
    escolha = str(input('Escolha Par ou ímpar [P/I]: ')).upper()[0].strip()
    if escolha == 'P':
        if res == 0:
            cont += 1
            print('-' * 30)
            print(f'\033[34mVocê jogou {pessoa} e o computador jogou {pc}. O resultado foi {soma}\033[m')
            print(f'\033[1;34mDeu PAR! Você venceu!\033[m')
        else:
            print('-' * 30)
            print(f'\033[31mVocê jogou {pessoa} e o computador jogou {pc}. O resultado foi {soma}\033[m')
            print(f'\033[1;31mDeu ímpar! Você perdeu!\033[m')
            break
    if escolha == 'I':
        if res == 1:
            cont += 1
            print('-' * 30)
            print(f'\033[34mVocê jogou {pessoa} e o computador jogou {pc}. O resultado foi {soma}\033[m')
            print(f'\033[1;34m Deu ÍMPAR! Você venceu!\033[m')
        else:
            print('-' * 30)
            print(f'\033[31mVocê jogou {pessoa} e o computador jogou {pc}. O resultado foi {soma}\033[m')
            print(f'\033[1;31mDeu PAR! Você perdeu!\033[m')
            break
print('-='*20)
print(f'\033[32mVocê venceu {cont} vezes seguidas!\033[m')
