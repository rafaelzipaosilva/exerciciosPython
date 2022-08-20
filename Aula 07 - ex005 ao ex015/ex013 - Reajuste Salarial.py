# Faça um algoritmo que leia o salário de um funcinário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Digite o valor do salário: R$'))
ns = sal + (sal * 0.15)

print('O salário de R${:.2f} foi atualizado em 15% e passou a ser de R${:.2f}'.format(sal, ns))