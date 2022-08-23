# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso (em Kg): '))
altura = float(input('Digite a sua altura (em metros): '))

imc = peso / (altura ** 2)

print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Classificado como \033[1:41mABAIXO DO PESO\033[m')
elif 18.5 <= imc < 25:
    print('Classificado como \033[1:32mPESO IDEAL\033[m')
elif 25 <= imc < 30:
    print('Classificado como \033[1:33mSOBREPESO\033[m')
elif 30 <= imc < 40:
    print('Classificado como \033[1:31mOBESIDADE\033[m')
else:
    print('Classificado como \033[1:41mOBESIDADE MÓRBIDA\033[m')
