# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
menor = 0
maior = 0
for c in range(1,8):
    nasc = int(input('Em que ano nasceu a {}ª pessoa: '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('''Deste grupo:
{} são maiores de idade.
{} são menores de idade'''.format(maior, menor))
