# estrutura aninhada:
'''
if carro.esquerda():
    bloco 1
elif carro.direita():
    bloco 2
elif carro.ré():
    bloco 3
else:
    bloco 4
'''

nome = str(input('Qual o seu nome: ')).upper().strip()

if nome == 'RAFAEL':
    print('Que nome bonito!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, \033[1:31m{}\033[m!'.format(nome))