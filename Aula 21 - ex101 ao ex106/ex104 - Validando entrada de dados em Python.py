'''
Crie um programa que tenha a função leiaInt(),
 que vai funcionar de forma semelhante 'a função input() do Python,
 só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''
def leiaint(valor):
    while True:
        if int(valor) is False:
            print(f'ERRO! Digite um valor numérico!')
        else:
            break

n = leiaint(input('Digite um número: '))
