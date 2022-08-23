# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('-=' * 20, '\n\033[1:31mCÁLCULO DE EMPRÉSTIMO\033[m')
print('-=' * 20)

valorcasa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
periodo = 12 * int(input('Quantos anos de financiamento: '))
vmensal = valorcasa / periodo
limite = salario * 0.30

if vmensal >= limite:
    print('\nSentimos muito! O seu empréstimo foi \033[1:31mNEGADO\033[m!')
    print('O valor mensal da casa seria de R$ {:.2f}.'.format(vmensal))
    print('De acordo com o seu salário, as parcelas não podem exceder R$ {:.2f}'.format(limite))
else:
    print('\nPARABÉNS! O seu empréstimo foi \033[1:32mAPROVADO\033[m!')
    print('O valor mensal da casa será de R$ {:.2f}.'.format(vmensal))
    print('O tempo para realizar o pagamento é de {} meses'.format(periodo))
