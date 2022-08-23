'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
 cadastrando tudo em uma lista composta.
Obs.: deixar com um 'delay' entre mostrar cada um dos palpites
'''
from time import sleep
from random import randint
lista = []
jogos = []
print('-' * 30)
print(f'      JOGA NA MEGA SENA      ')
print('-' * 30)
n = int(input('Quantos jogos você quer fazer? '))
print('-' * 30)

for t in range(0, n):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    cont = 0
    lista.clear()

print('>'*3, f'  CALCULANDO {n} JOGOS  ','<' * 3)
sleep(1)
for t in range(0, n):
    print(f'Jogo {t+1}: {jogos[t]}')
    sleep(1)
print('>' * 6, f'  BOA SORTE!  ','<' * 6)
