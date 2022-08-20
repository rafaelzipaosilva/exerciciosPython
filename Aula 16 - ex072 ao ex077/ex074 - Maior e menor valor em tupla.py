#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#  Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
sorteio = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior = menor = 0
for c in range(0, 5):
    if sorteio[c] > maior:
        maior = sorteio[c]
    if menor == 0:
        menor = sorteio[c]
    elif sorteio[c] < menor:
        menor = sorteio[c]

print(f'Os números sorteados são: {sorteio}')
print(f'O menor valor sorteado é o {menor}')
print(f'O maior valor sorteado é o {maior}')
#forma direta pelos métodos das tuplas
print(f'O menor valor sorteado é o {min(sorteio)}')
print(f'O maior valor sorteado é o {max(sorteio)}')
