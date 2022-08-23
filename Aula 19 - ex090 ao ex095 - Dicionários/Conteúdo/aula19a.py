#Dicionários
'''
dados = list() #criar uma lista vazia
dados.append('Pedro') #adicionar um valor
print(dados[0]) #imprime o índice 0 na lista dados

#Dicionários você personaliza os itens de uma lista

#Declaração de listas
Tupla = ()
Lista = []
Dicionário = {}

dados = dict()
dados = {'nome':'Pedro','idade': 25}
print(dados['nome'] #Pedro
print(dados['idade'] #25
#Para adicionar um novo ítem no dicionário:
dados['sexo']='M' #adiciona um novo campo com um item no dicionário
del dados['idade'] #exclui o 'campo' idade do dicionário Dados
'''

'''
filme = {'título': 'Star Wars',
         'ano' : 1977,
         'diretor': 'George Lucas'
        }

for k, v in filme.items():
    print(f'O {k} é {v}')

print(filme)
print(filme.values()) #imprime os valores do dicionário
print(filme.keys()) #imprime as chaves utilizadas no dicionário
print(filme.items()) #imprime todos os itens do dicionário
'''

'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.items())
print(pessoas.values())
print(pessoas.keys())
pessoas['nome'] = 'Leandro' #modifica um valor de um dicionário
pessoas['peso'] = 98.5 #Adiciona um novo valor ao dicionário

for k, v in pessoas.items():
    print(f'{k} = {v}')
'''

'''
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
'''

'''estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()'''

'''from random import randint
from operator import itemgetter #utilizar para conseguir colocar em ordem um dicionário
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jodador4': randint(1, 6)}
ranking = list() #a ordenação acontece para uma nova lista, por isso é necessário criar uma nova lista
print('==  VALORES SORTEADOS  ==')
for k, v in jogo.items(): #laço para criar o random de números
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True) #a função importada itemgetter trata como lista, por isso utilizar a posição 1 para indicar qual quer utilizar.
print('==  RANKING DOS JOGADORES  ==')
for i, v in enumerate(ranking):
    print(f'{i+1}ºlugar: {v[0]} com {v[1]}.')'''