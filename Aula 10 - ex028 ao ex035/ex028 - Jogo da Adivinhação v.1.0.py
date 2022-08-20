# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
npc = randint(0, 5)
print('O computador escolheu um número entre 0 e 5')
nu = int(input('Qual número você acha que foi? '))
print('PROCESSANDO...')
sleep(3)
if npc == nu:
    print('VOCÊ VENCEU! Acertou o número que o computador escolheu!')
else:
    print('VOCÊ PERDEU! O computador escolheu o número {}'.format(npc))