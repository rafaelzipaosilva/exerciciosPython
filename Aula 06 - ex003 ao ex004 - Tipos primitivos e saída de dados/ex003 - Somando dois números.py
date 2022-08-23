# Crie um programa que leia dois numeros e mostre a soma entre eles
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
cores = {'l':'\033[m', 'c1':'\033[36m', 'c2':'\033[32m', 'cr':'\033[1:37m'}
print('A soma entre os números {}{}{} e {}{}{} é {}{}{}'.format(cores['c1'], n1, cores['l'], cores['c2'] , n2,cores['l'], cores['cr'], s, cores['l']))
