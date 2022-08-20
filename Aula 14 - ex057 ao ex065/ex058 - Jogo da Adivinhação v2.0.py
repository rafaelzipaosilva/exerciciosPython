#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
pc = randint(0, 10)
jogador = ''
cont = 0
print('O COMPUTADOR ESCOLHEU UM NÚMERO DE 0 À 10.')
print('Será que você consegue acertar?')
while jogador != pc:
    jogador = int(input('Qual o seu palpite? (De 0 à 10): '))
    cont +=1
    if jogador != pc:
        # para facilitar adivinhar o resultado
        if jogador > pc:
            print('Menos... Tente mais uma vez!')
        elif jogador < pc:
            print('Mais... Tente mais uma vez!')
if cont == 1:
    print('Parabéns! Você acertou com apenas {} palpite!'.format(cont))
else:
    print('Sensacional! Foram necessários {} palpites para acertar!'.format(cont))
