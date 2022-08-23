'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
 guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

pessoa = dict()
grupo = list()
totidade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    totidade += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if r in "SN":
            break
        print('ERRO! Responda apenas S ou N.')
    if r == 'N':
        break
media = totidade/len(grupo)

print(grupo)

print('=-'*30)
print(f'A) Foram cadastradas {len(grupo)} pessoas.')
print(f'B) A média de idade é {media:.2f}.')
print(f'C) As mulheres castradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}... ', end='')
print()
print('D) As pessoas com idade acima da média:')
'''for p in grupo:
    if p['idade'] >= media:
        print(f'   - Nome: {p["nome"]}, Sexo: {p["sexo"]}, Idade: {p["idade"]} anos.')
'''
for p in grupo:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k}: {v}, ', end='')
        print()
print('<< ENCERRADO >>')