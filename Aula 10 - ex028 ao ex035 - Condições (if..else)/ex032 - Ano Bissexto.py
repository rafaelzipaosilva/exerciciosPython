# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# para um ano ser bissexto ele precisa:
# se for dividido por 4 precisa dar um número inteiro
# se dividido por 100 der um numero inteiro e divido por 400 for inteiro é um ano bissexto
# se divido por 100 der um numero inteiro e divido por 400 não der um numero inteiro, não é um ano bissexto
from datetime import date
ano = int(input('Que ano quer analisar? Coloqe 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
