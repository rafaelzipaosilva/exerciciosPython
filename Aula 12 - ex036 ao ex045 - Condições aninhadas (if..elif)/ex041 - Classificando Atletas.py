# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

if idade <= 9:
    print('Sua idade no fim do ano será de {}.\nCategoria MIRIM'.format(idade))
elif idade <= 14:
    print('Sua idade no fim do ano será de {}.\nCategoria INFANTIL'.format(idade))
elif idade <=19:
    print('Sua idade no fim do ano será de {}.\nCategoria JUNIOR'.format(idade))
elif idade <= 25:
    print('Sua idade no fim do ano será de {}.\nCategoria SENIOR'.format(idade))
else:
    print('Sua idade no fim do ano será de {}.\nCategoria MASTER'.format(idade))
