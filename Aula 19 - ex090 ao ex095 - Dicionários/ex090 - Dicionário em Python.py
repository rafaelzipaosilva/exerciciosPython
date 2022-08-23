'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

aluno = {}

while True:
    aluno['Nome'] = str(input('Nome: '))
    aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
    if aluno['Média'] >= 7.0:
        aluno['Situação'] = 'APROVADO'
    elif 5 <= aluno['Média'] < 7:
        aluno['Situação'] = 'RECUPERAÇÃO'
    else:
        aluno['Situação'] = 'REPROVADO'
    print('=-' * 30)
    for k, v in aluno.items():
        print(f'  - {k} é igual a {v}')
    print('=-' * 30)
    r = str(input('Deseja cadastrar outro aluno? [S/N]: '))
    print('=-' * 30)
    if r in 'Nn':
        break

print('Obrigado por usa o nosso sistema!')