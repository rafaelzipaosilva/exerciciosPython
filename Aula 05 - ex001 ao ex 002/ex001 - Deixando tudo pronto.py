# Escrever um script que envie a msg Olá, mundo!
cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'verde':'\033[32m'}

print('Olá, {}Mundo{}!'.format(cores['verde'], cores['limpa']))
