# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual o salário do funcionário: R$'))

if sal <= 1250.00:
    novo = sal * 1.15
    print('Salário atual: R$ {:.2f}\nVocê terá um aumento de 15%\nSeu novo salário será R$ {:.2f}'.format(sal, novo))
else:
    novo = sal * 1.10
    print('Salário atual: R$ {:.2f}\nVocê terá um aumento de 10%\nSeu novo salário será R$ {:.2f}'.format(sal, novo))
