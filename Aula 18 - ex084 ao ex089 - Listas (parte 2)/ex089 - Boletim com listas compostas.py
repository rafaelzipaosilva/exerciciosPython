'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
Obs.: Estrutura com 3 niveis de lista composta
'''
'''
#SOLUÇÃO RAFAEL
mascara = [[],[],[]]
alunos = []
notas = [0.0, 0.0]
media = escolha = 0
while True:
    mascara[0] = str(input('Nome: '))
    for n in range(0, 2):
        notas[n] = float(input(f'Digite a {n+1}ª nota: '))
        media += notas[n]
    mascara[1] = notas[:]
    media = media / 2
    mascara[2] = media
    alunos.append(mascara[:])
    print('Aluno cadastrado com sucesso!')
    r = (str(input('Deseja adicionar mais um aluno? [S/N] ')))
    if r in 'Nn':
        break

while True:
    print()
    print('=-' * 15)
    print(f'Lista de Alunos')
    print('=-' * 15)
    for a in range(0, len(alunos)):
        print(f'{a:<3} - {alunos[a][0]:<} - Média: {alunos[a][2]}')
    print('=-'* 15)
    escolha = int(input('De qual alunos você gostaria de receber mais detalhes? '))
    print(f'Nome do alunos: {alunos[escolha][0]}')
    print(f'Nota 1: {alunos[escolha][1][0]}')
    print(f'Nota 2: {alunos[escolha][1][1]}')
    print(f'Média: {alunos[escolha][2]}')
    r = str(input('Gostaria de consultar mais algum aluno? [S/N]? '))
    if r in 'Nn':
        print('Muito obrigado por utilizar o nosso sistema!')
        break

'''

#SOLUÇÃO DO GUANABARA
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar nota de qual alunos? '))
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        print('FINALIZANDO...')
        break
print('<' * 5,' VOLTE SEMPRE! ', '>' * 5)