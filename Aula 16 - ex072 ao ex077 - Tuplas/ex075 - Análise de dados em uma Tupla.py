# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numeros = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))
print(f'Você digitou os valores {numeros}')
if 9 in numeros:
    print(f'O número 9 aparece {numeros.count(9)} vezes.')
else:
    print('O número 9 não aparece nenhuma vez')
if 3 in numeros:
    print(f'O número 3 foi digitado pela primeira vez na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não aparece em nenhuma posição.')
print('Os valres pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
