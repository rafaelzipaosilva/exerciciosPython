'''
#revisão da aula 17
dados = list() #criar uma lista vazia
dados.append('Pedro') #adiciona um item no indice 0 da lista
dados.append(25) #adiciona um item no indice 1 da lista
print(dados[0]) #mostra os dados no indice 0 da lista. No caso, Pedro
print(dados[1]) #mostra os dados no indice 1 da lista. No caso, 25
'''
'''
pessoas = list()
pessoas.append(dados[:]) #adiciona a lista dados dentro do indice 0 da lista pessoas
'''
'''
#criar uma lista composta
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) #resultado Pedro
print(pessoas[1][1]) #resultado 19
print(pessoas[2][0]) #resultado João
print(pessoas[1]) #imprime o indice 1 integralmente: ['Maria', 19]
'''
'''
#adicionar dois registros em uma lista composta
teste = list()
teste.append('Gustavo')
teste.append(40)
g1 = list()
g1.append(teste[:]) #ao colocar o [:] estou indicando para adicionar uma cópia da lista 'teste' na lista 'G1'
teste[0]= 'Maria'
teste[1]= 22
g1.append(teste[:]) #ao colocar novamente o [:] ele adiciona um novo item na lista 'G1' com os novos dados
print(g1)
'''
'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] #adiconando a estrutura composta de 4 itens na estrura principal
print(galera[0]) #imprime toda a estrutura composta do indice 0
print(galera[0][0]) #imprime apenas o indice 0 da estrutura composta no indice 0

#comando para imprimir a lista de todos os valores
for p in galera:
    print(p)

#comando para imprimir apenas o indice 0 da estrutura composta galera, no caso, os nomes
for p in galera:
    print(p[0])

#comando para imprimir apenas o indice 1 da estrutura composta galera, no caso, a idade
for p in galera:
    print(p[1])

#comando para imprimir a estrutura composta de uma forma mais fácil de se entender
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
'''
'''
galera = [] #é a estrutura principal
dado = [] #funciona como uma estrutura auxiliar para preencher a estrutura principal
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #adiciona uma cópia de dado na lista galera. Se esquecer de colocar [:] ele fica vinculado e no comando clear ele vai apagar todos os dados digitados, deixando apenas uma lista vazia.
    dado.clear() #limpa a lista dado para a nova adição

#analise para saber quantos são maiores e quantos são menores de idade
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade')
'''
