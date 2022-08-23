# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao total (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()

print('Analisando o nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
separa = nome.split()

print('Seu tem ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome é {} e ele tem tem {} letras'.format(separa[0], len(separa[0])))
