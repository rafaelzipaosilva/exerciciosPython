# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = cont = media = maior = menor = 0
n = 0
resp = 'S'

while resp in 'sS':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja escrever outro número? [S/N]: ')).upper().strip()[0]

media = soma / cont
print('\nA média dos números digitados é {:.2f}.'.format(media))
print('O menor número digitado foi o {}.'.format(menor))
print('O maior número digitado foi o {}.'.format(maior))
