# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor do produto: R$ '))
pgto = int(input('''Escolha a forma de pagamento:
[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))

if pgto == 1:
    total = valor * 0.9
elif pgto == 2:
    total = valor * 0.95
elif pgto == 3:
    parcela = valor / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros.'.format(valor, parcela))
elif pgto == 4:
    total = valor * 1.2
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcela em {}x de R$ {:.2f} com juros de 20%.'.format(totalparc, parcela))
else:
    total = valor
    print('OPÇÃO INVÁLIDA. Escolha outra opção de pagamento!')
print('Sua compra de R$ {:.2f} passou a custar R$ {:.2f} no final'.format(valor, total))
