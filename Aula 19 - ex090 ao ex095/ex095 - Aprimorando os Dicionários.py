'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
 incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
partidas = list()
jogador = dict()
time = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Número de partidas de {jogador["Nome"]}: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {c + 1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        r = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N!')
    if r == 'N':
        break

while True:
    print('-' * 45)
    print('Cód.  ', end='')
    for i in jogador.keys():
        print(f'{i:<15} ', end='')
    print()
    print('-' * 45)
    for k, v in enumerate(time):
        print(f'{k:<5} ', end='')
        for d in v.values():
            print(f'{str(d):<15} ', end='')
        print()
    print('-' * 45)

    while True:
        busca = int(input('Mostrar dados de qual jogador? '))
        if busca >= len(time):
            print('ERRO! Jogador não existe!')
        else:
            print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: --')
            for i, g in enumerate(time[busca]['Gols']):
                print(f'  No jogo {i+1} fez {g} gols.')
            print('-' * 45)
            break

    while True:
        fim = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Digite apenas S ou N!')
    if fim == 'N':
        break
print('<< PROGRAMA ENCERRADO! VOLTE SEMPRE! >>')
