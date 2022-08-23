# Crie um programa que faça o computador jogar Jokenpô com você.

#[1] pedra
#[2] papel
#[3] tesoura

from random import randint
from time import sleep
itens = ('PEDRA','PAPEL','TESOURA')
pc = randint(0, 2)
print('Vamos jogar jo-ken-pô?')
eu = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual a sua opção? '''))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

if pc != 0 != 1 != 2 != pc:
    print('-=' * 11)
    print('''Computador = {}
    Você = {}'''.format(itens[eu], itens[pc]))
    print('-=' * 11)
    if pc == 0: #PC jogou PEDRA
        if eu == 0: #JOGADOR jogou PEDRA
            print('O JOGO EMPATOU!')
        elif eu == 1: #JOGADOR jogou PAPEL
            print('O JOGADOR VENCEU!')
        elif eu == 2: #JOGADOR jogou TESOURA
            print('O COMPUTADOR VENCEU!')
    elif pc == 1: #PC jogou PAPEL
        if eu == 0: #JOGADOR jogou PEDRA
            print('O COMPUTADOR VENCEU!')
        elif eu == 1: #JOGADOR jogou PAPEL
            print('O JOGO EMPATOU!')
        elif eu == 2: #JOGADOR jogou TESOURA
            print('O JOGADOR VENCEU!')
    elif pc == 2: #PC jogou TESOURA
        if eu == 0: #JOGADOR jogou PEDRA
            print('O JOGADOR VENCEU!')
        elif eu == 1: #JOGADOR jogou PAPEL
            print('O COMPUTADOR VENCEU!')
        elif eu == 2: #JOGADOR jogou TESOURA
            print('O JOGO EMPATOU!')
else:
    print('JOGADA INVÁLIDA')

''' OUTRA OPÇÃO DE RESOLUÇÃO
if pc == eu:
    print('DEU EMPATE')
elif pc == 0 and eu == 2 or pc == 1 and eu == 0 or pc == 2 and eu == 1:
    print('O computador ganhou!')
elif eu == 0 and pc == 2 or eu == 1 and pc == 0 or eu == 2 and pc == 1:
    print('Vocé ganhou. Parabéns!')
'''