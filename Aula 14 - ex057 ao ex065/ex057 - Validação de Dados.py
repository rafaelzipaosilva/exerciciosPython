# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
from time import sleep
sexo = ''
while sexo != 'F' != 'M' != sexo:
    sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()[0]
    if sexo != 'M' != 'F' != sexo:
        print('Por favor, digite o sexo correto!')
        sleep(1)
print('Sexo digitado corretamente! Muito obrigado!')