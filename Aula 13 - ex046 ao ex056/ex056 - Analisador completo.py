# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
#  - a média de idade do grupo,
#  - qual é o nome do homem mais velho e
#  - quantas mulheres têm menos de 20 anos.
soma = 0
mediaidade = 0

nomevelho = ''
maioridadehomem = 0

totmulher20 = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma += idade

    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F':
        if idade < 20:
            totmulher20 += 1
mediaidade = soma / 4
print('A média de idade do grupo é {:.2f}.'.format(mediaidade))
print('O nome do homem mais velho é {}'.format(nomevelho))
print('{} mulheres tem menos de 20 anos'.format(totmulher20))
