# Atribuição dos dados em um 'mini-espaço' do computador e vai receber um índice
# Esse índice vai de '0' até o último digito
frase = 'Curso em Vídeo Python'
print(frase) # Imprime a frase inteira
# obs.: Cada espaço conta como um índice
# obs.: O Python é Key Sensitive, ou seja, uma letra maiuscula é diferente da mesma letra minuscula

# FATIAMENTO - Lida diretamente com o indice de cada caracter da frase
print('\nEXEMPLOS DE FATIAMENTO')
print('Ex1: ', frase[9]) # pega apenas o indice 9
print('Ex2: ', frase[9:13]) # pega a faixa entre os indices 9 e 12
print('Ex3: ', frase[9:21:2]) # pega a faixa entre os indices 9 e 20, pulando de 2 em 2
print('Ex4: ', frase[:5]) # pega do inicio e vai até o indice 4
print('Ex5: ', frase[15:]) # pega do indice 5 até o final
print('Ex6: ', frase[9::3]) # do indice 9 até o final pulando de 3 em 3 indices
print('Ex7: ', frase[::2]) # pega a string inteira e vai pulando de 2 em dois índices

# ANÁLISE - lida diretamente com os elementos da frase
print('\nEXEMPLOS DE ANÁLISE')
print('Ex1: ', len(frase)) # mostra o comprimento da frase, em número de caracteres
print('Ex2: ', frase.count('o')) # conta quantas vezes a letra 'o' aparece na frase.
print('Ex3: ', frase.count('o', 0, 13)) #faz a contagem já com o fatiamento entre os indices 0 e 12
print('Ex4: ', frase.find('deo')) # retorna em que indice inicia primeira vez a sequencia 'deo' na frase
print('Ex5: ', frase.find('Android')) # Se a busca não tiver um resultado compatível, o resultado exibido será '-1', indicando que não está presente a qtde
print('Ex6: ', 'Curso' in frase) # retorna True ou False se a sentença existe na frase

# TRANSFORMAÇÃO
print('\nEXEMPLOS DE TRANSFORMAÇÃO')
# obs.: a transformação acontece apenas na exibição
# obs.: para gravar a transformação na variável é necessário falar para o python fazer a sobreinscrição
print('Ex1: ', frase.replace('Python', 'Android')) # substituiu as palavras na EXIBIÇÃO, mas não na variável
print('Ex2: ', frase.upper()) # transforma todos os caracteres em maiúsculas
print('Ex3: ', frase.lower()) # transforma todos os caracteres em minúsculas
print('Ex4: ', frase.capitalize()) # transforma todos os caracteres em minúsculo e apenas o 1º da frase em maiúsculo
print('Ex5: ', frase.title(), '\n') # transforma o primeiro caractere de cada palavra em maiunsculo e o restante em minúsculo

frase2 = '   Aprendendo Python  '
print('Ex6: ', frase2.strip()) # remove espaços excedentes do inicio e do final da frase
print('Ex7: ', frase2.rstrip()) # remove os espaços excentes que estão à direita da frase
print('Ex8: ', frase2.lstrip()) # remove os espaços excentes que estão à esquerda da frase

# DIVISÃO
print('\nEXEMPLOS DE DIVISÃO')
print('Ex1: ', frase.split()) # divide a string em uma lista, sempre recebendo um novo indice para cada item

# JUNÇÃO
print('\nEXEMPLOS DE JUNÇÃO')
frase3 = frase.split()
print('Ex1: ', '-'.join(frase3)) # junta a lista criada com o split, utilizando o separador '-' entre as palavras.
print('Ex2: ', '-'.join(frase)) # se for utilizada com a string inteira, ele irá coloca o separador '-' entre cada um dos indices


# MESCLAGEM DE FUNÇÕES EM OBJETOS
print('\nEXEMPLOS DE MESCLAGENS DENTRO DE OBJETOS')
print(frase)
print('Ex1: ', frase.upper().count('O')) # Alterando os caracteres para maiúscula e depois contando os 'O'
print('Ex2: ', frase.lower().find('vídeo')) # Altera todos os caracteres para minúscula e procura a posição inicial da palavra 'vídeo'
print('Ex3: ', len(frase2.strip())) # contar a qtde de indices de uma frase, retirando os espaços excedentes
print('Ex4: ', frase2.replace('Python','Android')) # exibe apenas a frase substituindo as palavras
frase2 = frase2.replace('Python','Android').strip() # grava na variavel as alterações do replace e do strip
print('Ex5: ', frase2) # exibindo o novo resultado da variável

# SPLIT - verificar outras funcionalidades que ficam dentro do parenteses do split
print('\nEXEMPLOS DE UTILIZAÇÃO DO SPLIT')
frase = 'Curso em Vídeo Python'
print(frase)
dividido = frase.split() # atribui em uma variavel a frase como lista
print('Ex1: ', dividido) # exibe a lista
print('Ex2: ', dividido[2]) #exibe o item do indice '2' da lista
print('Ex3: ', dividido[2][3]) # exibe o indice '3' da palavra que está no indice 2 da lista
