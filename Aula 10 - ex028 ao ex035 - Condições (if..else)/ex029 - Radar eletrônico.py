# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('EXCESSO DE VELOCIDADE!!! \nO seu carro foi multado em R$ {:.2f}.'.format(multa))
else:
    print('Dentro da velocidade!')
