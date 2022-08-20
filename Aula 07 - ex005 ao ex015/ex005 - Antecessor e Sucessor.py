# Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e o seu antecessor

# variáveis
n = int(input('Digite um número: '))

# cores
cores = {'l':'\033[m', 'ca':'\033[36m', 'cs':'\033[37m', 'cn':'\033[1:31m'}
# impressão do resultado
print('O número digitado é o {}{}{}\n. O antecessor é o {}{}{}\n. O sucessor é o {}{}{}'.format(cores['cn'], n,cores['l'], cores['ca'], (n-1),cores['l'], cores['cs'], (n+1), cores['l']))
