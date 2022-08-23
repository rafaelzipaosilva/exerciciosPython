#Intercative Help
'''
help(print)
print(input.__doc__)'''

#docstrings
'''#ajuda para mostrar a documentação de cada função
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c=i
    while c<=f:
        print(f'{c} ',end='')
        c+=p
    print('FIM!')


help(contador)'''

#Argumentos opcionais
'''def somar(a,b,c=0): #colocar o '=0' que deixa o parametro como opcional
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terciero valor (opcional)
    """
    s=a+b+c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)'''

#Escopo de variáreis
'''#Ex1:
def teste():
    x = 8 #x está no escopo local, que só funciona nesta parte do programa
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')

n = 2 #n está no escopo global, que funciona no programa inteiro.
print(f'No programa principal, n vale {2}.')
teste()

#Ex2:
def teste(b):
    a=8 #crio a variavel A com um escopo local
    b+=4
    c=2
    print(f'A dentro vale {a}') #funciona por ser escopo global. SE ela for redefinida dentro do def, passa a assumir esse valor.
    print(f'B dentro vale {b}') #funciona por ser escopo local
    print(f'C dentro vale {c}') #funciona por ser escopo local


a=5
teste(a)
print(f'A fora vale {a}') #funciona por ser escopo global
#print(f'B fora vale {b}') #NÃO FUNCIONA, por ser escopo local de teste()
#print(f'C fora vale {c}')#NÃO FUNCIONA, por ser escopo local de teste()

#Ex3:
def teste(b):
    global a #faz com que se utilize a variável global dentro da def.
    a=8
    b+=4
    c=2
    print(f'A dentro vale {a}') #funciona por ser escopo global.
    print(f'B dentro vale {b}') #funciona por ser escopo local
    print(f'C dentro vale {c}') #funciona por ser escopo local


a=5
teste(a)
print(f'A fora vale {a}') #funciona por ser escopo global'''

#Retorno de resultados
'''def somar(a=0, b=0, c=0):
    s = a+b+c
    return s #para que o resultado seja utilizado fora da função, deve ser utilizado o return.


r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')'''

#Exemplo 1 - utilizando o return
'''def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''

#Exemplo 2 - utilizando o return
'''def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')'''

#Exemplo 3 - resultado booleano
'''def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num)) #mostra o resultado de verdadeiro ou falso
if par(num):
    print('É par!')
else:
    print('Não é par!')'''
