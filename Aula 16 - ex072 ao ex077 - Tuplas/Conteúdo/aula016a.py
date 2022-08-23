'''
Variáveis compostas:
Tuplas, listas e dicionários

Fatiamento de tuplas é igual ao fatiamento de strings:
Ex.:
lanche[2] - pega somente esta posição da tupla
lanche[0:2] - pega os itens da posição 0 até a posição 1 (excluindo a ultima posição)
lanche[1:] - pega da posição 1 até o final
lanche[-1] - pega o item pela posição inversa
len(lanche) - retorna o número de posições contidas na variavel
for c in lanche: (sem o range) - para retornar as posições de lanche no laço de repetição
    print(c)

TUPLAS SÃO IMUTÁVEIS - vc não consegue alterar um tupla durante a execução do programa.
'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# TUPLAS SÃO IMUTÁVEIS
# Formas de utilização de tuplas
print(lanche[1])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2])
print(lanche[-3:])
print(lanche)
len(lanche)

# usando um for para imprimir direto
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

# usando o enumerate para saber a posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

# usando uma variável de contador pra saber a posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

print(sorted(lanche)) #muda pra colocar em ordem


a = (2, 5, 4)
b = (5, 8, 1, 2)

c = a + b #pega a tupla a e concatena com a tupla b
print(c)

d = b + a #pega a tupla b e concactena com a tupla a
print(d)

print(len(c)) # número de posições da tupla
print(c.count(5)) # conta quantos elementos possuem na tupla de acordo com o que foi solicitado
print(d.index(5)) # retorna a posição da ocorrencia do termo
print(d.index(5, 1)) #retorna a posição da ocorrencia de acordo com uma posição especifica

# tupla pode ter elementos diferentes: int, string, etc
# você só pode deletar uma tupla inteira, não consegue deletar só uma parte dela.