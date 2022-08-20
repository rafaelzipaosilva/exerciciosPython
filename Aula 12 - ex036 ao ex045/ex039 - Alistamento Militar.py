# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - se ele ainda vai se alistar ao serviço militar,
# - se é a hora exata de se alistar ou
# - se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
print('\033[7;40mSERVIÇO DE ALISTAMENTO MILITAR {}\033[m'.format(atual))
ano = int(input('Digite o ano de nascimento com 4 digitos: '))
idade = atual - ano

if idade == 18:
    print('Você precisa se alistar este ano!')
elif idade < 18:
    print('Você ainda não precisa de alistar.')
    print('Seu alistamento será daqui a {} ano(s). NÃO SE ESQUEÇA!'.format(18 - idade))
else:
    print('Você já passou do tempo de se alistar!')
    print('Era pra ter se alistado há {} ano(s)'.format(idade - 18))
