# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Conside US$1.00=R$3.27

r = float(input('Quanto dinheiro você tem na carteira? R$'))

print('Com R${:.2f} você pode comprar USD{:.2f}'.format(r, r/5.67))
print('Com R${:.2f} você pode comprar EUR{:.2f}'.format(r, r/6.43))
print('Com R${:.2f} você pode comprar LIB{:.2f}'.format(r, r/7.60))