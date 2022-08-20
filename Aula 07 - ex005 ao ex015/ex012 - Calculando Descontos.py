# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

preco = float(input('Adicione o valor do produto: R$'))
np = preco - (preco * 0.05)

print('O produto que custava R${:.2f} teve um desconto de 5% e passou a custar R${:.2f}'.format(preco, np))
