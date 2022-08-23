'''
Listas são mutáveis e possuem vários métodos que só funcionam para elas
'''
'''
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[3] = 'picolé'# para substitui um item da lista
print(lanche)
lanche.append('cookie') #cria um novo elemento no FINAL DA LISTA
print(lanche)
lanche.insert(0, 'cachorro quente') #abre um espaço na posição 0 da lista. Os itens contidos na lista são afastados e renumerados
print(lanche)
'''
'''
# removendo um item da lista
del lanche[3] # a paga o item da lista indicando indice
lanche.pop(3) # apaga o item da lista indicando o indice
lanche.pop() # remove o ultimo elemento da lista
lanche.remove('pizza') # apaga o item da lista indicando o conteudo
if 'pizza' in lanche: # verifia a existencia do elemento na lista antes de tentar remover
    lanche.remove('pizza')
'''
''' 
# criar listas
val = list(range(4,11)) #criar uma lista a partir de um range organizado
valores = [8, 2, 5, 4, 9, 3, 0] #lista criada de forma aleatoria
valores.sort() #ele ordena os valores dentro da lista
valores.sort(reverse=True) # ordena os valores em ordem reversa
len(valores) #retorna a qtde de elementos da lista
'''
'''
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
'''

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for v in valores:
    print(f'{v}...', end='')
print('\n')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista')

'''
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digie um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista')
'''
'''
a = [2, 3, 4, 7]
b = a #ao fazer esse tipo de atribuição vc cria uma ligação entre as listas
b = a[:] # para criar uma cópia da lista precisa usar o método de fatiamento
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''