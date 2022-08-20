'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
 e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''

def notas(* nts):
    lista = dict()
    lista['qtde'] = len(nts)
    for n in nts:
        if n == 0:
            lista['menor'] = n
            lista['maior'] = n
        else:
            if n > lista['maior']:
                lista['maior'] = n
            elif lista['menor'] < n:
                lista['menor'] = n
        soma += n
    lista['media'] = soma / lista['qtde']
    print(lista)



notas(5, 45, 14, 45)