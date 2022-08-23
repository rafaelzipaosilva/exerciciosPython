'''
MODULARIZAÇÃO
- dividir um programa grande
- aumentar a legibilidade
- facilitar a manutenção

- criar uma nova pasta
- colocar o arquivo com o programa principal nesta pasta
- criar o arquivo com as funcionalidades dentro da mesma pasta
- chamar o arquivo com as funcionalidades dentro do arquivo principal, utilizando o import

VANTAGENS
- organização do código
- facilidade na manutenção
- ocultação de código detalhado
- reutilizar em outros projetos

PACOTES
- conjunto de módulos
- criar um pacote estruturado em pastas
- toda pasta de pacotes tem que ter o arquivo chamado __init__.py

'''

'''
#utilizando a importação de um módulo
import uteisAula22a

num = int(input('Digite um valor: '))
fat = uteisAula22a.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteisAula22a.dobro(num)}')
print(f'O triplo de {num} é {uteisAula22a.triplo(num)}')'''

from uteis import numeros


num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')