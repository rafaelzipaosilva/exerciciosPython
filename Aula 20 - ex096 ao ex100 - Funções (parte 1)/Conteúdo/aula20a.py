'''
Funções = rotinas (coisas que são feitas com frequência)
Ex.: print(), len(), input(), int(), float()

*criar uma função utilizando uma DEF, ex: adicionar uma linha

def mostralinha():
    print('=-' * 30)
'''
'''def linha():
    print('=-' * 15)
def mensagem(msg):
    print('=-' * 15)
    print(f'{msg:^30}')
    print('=-' * 15)


mensagem('SISTEMA DE ALUNOS')
mensagem('OI')
mensagem('MEU NOME É RAFAEL')'''
'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print()


soma(4, 5)
soma(b=4, a=5)'''
'''def cont1(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim!')

def cont2(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


cont1(2, 1, 7)
cont2(1, 2)
cont1(5, 1, 2, 5, 7)'''
'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print()
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} tenmos {s}')


valores = [5, 3, -5, 125]
dobra(valores)
print(valores)
soma(4, 5, 5)
soma(3, 15, -9, 17, 102)'''

