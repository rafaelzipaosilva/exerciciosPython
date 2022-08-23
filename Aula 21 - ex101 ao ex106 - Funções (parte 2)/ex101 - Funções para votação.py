'''
Crie um programa que tenha uma função chamada voto() que
 vai receber como parâmetro o ano de nascimento de uma pessoa,
 retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
 de 16 à 17 anos, e, 65 anos: voto opcional
'''
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'{idade} anos: NÃO VOTAS!'
    elif 16 <= idade < 18 or idade >= 65:
        return f'{idade} anos. VOTO OPCIONAL!'
    else:
        return f'{idade} anos: VOTO OBRIGATÓRIO!'


#Programa principal:
nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
