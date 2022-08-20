# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distância da sua viagem: '))

if distancia <= 200:
    preco = distancia * 0.50
    print('Sua viagem tem até 200Km de distância.\nO valor da sua passagem é de R$ {:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('Sua viagem tem mais de 200Km de distância.\nO valor da sua passagem é de R$ {:.2f}'.format(preco))
