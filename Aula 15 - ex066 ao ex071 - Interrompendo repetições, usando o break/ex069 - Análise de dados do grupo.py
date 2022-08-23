# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#   A) quantas pessoas tem mais de 18 anos.
#   B) quantos homens foram cadastrados.
#   C) quantas mulheres tem menos de 20 anos.
cad = cmaiores = cmulher = chomem = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Idade? '))
    cad += 1
    if idade >= 18:
        cmaiores += 1
    if sexo == 'M':
        chomem += 1
    if sexo == 'F' and idade < 20:
        cmulher += 1
    print('-'*30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*20)
print(f'Foram cadastradas {cad} pessoas. Este é resultado:')
print(f'{cmaiores} pessoas são maiores.')
print(f'Foram cadastrados {chomem} homens.')
print(f'Foram cadastradas {cmulher} mulheres com menos de 20 anos.')
print('+='*20)
