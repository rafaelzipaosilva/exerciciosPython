# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza)

nome = str (input('Digite seu nome completo: ')).strip()
print('O nome é : {}'.format(nome))
print('O primeiro nome é {}'.format(nome[:nome.find(' ')].title()))
print('O último nome é {}'.format(nome[nome.rfind(' ')+1:].title()))