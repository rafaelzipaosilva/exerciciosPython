# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tab = int(input('Escolha um número para mostrar a tabuada: '))
print('Tabuada do {}'.format(tab))
for c in range(1, 11):
    print('{} x {:>2} = {:>3}'.format(tab, c, c * tab))