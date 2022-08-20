'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho, e,
 cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime
funcionario = dict()
funcionario['Nome'] = str(input('Nome do funcionário: '))
funcionario['Nascimento'] = int(input('Ano de nascimento (ex. 1996): '))
funcionario['Idade'] = datetime.now().year - funcionario['Nascimento']
funcionario['CTPS'] = int(input('Número da Carteira de trabalho (0 não tem): '))
if funcionario['CTPS'] != 0:
    funcionario['Contratação'] = int(input('Ano de contratação: '))
    funcionario['Aposentadoria'] = funcionario['Idade'] + ((funcionario['Contratação'] + 35) - datetime.now().year)
    funcionario['Salário'] = float(input('Salário: R$'))
print('==  DADOS DO FUNCIONÁRIO  ==')
for k, v in funcionario.items():
    print(f'{k}: {v}')
