# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='¬ ')
print('ACABOU')

# outra solução
'''
n = int(input('Digite o primeiro termo: '))
r = int(input('Escolha a razão da P.A: '))
for c in range (1,11):
    print('{}º termo: {}'.format(c, n))
    n = n + r
'''