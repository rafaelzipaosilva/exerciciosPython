# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    tab = int(input('Qual tabuada você quer ver? '))
    print('-'*30)
    if tab < 0:
        break
    print(f'Tabuada do {tab}')
    for c in range(1, 11):
        print(f'{tab} * {c} = {tab * c}')
    print('-'*30)
print('Programa finalizado com sucesso!')
