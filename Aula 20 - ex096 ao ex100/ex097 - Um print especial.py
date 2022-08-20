'''
Faça um programa que tenha uma função chamada escreva(),
 que receba um texto qualquer como parâmetro
  e mostre uma mensagem com tamanho adaptável.

Ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~
'''
def escreva(msg):
    tam = len(msg) + 4
    print(f'~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)
    print()


#Programa principal
escreva('Olá, Mundo!')
escreva('Vida longa e próspera')
escreva('Nada melhor que o amanhã!')
escreva('CeV')
