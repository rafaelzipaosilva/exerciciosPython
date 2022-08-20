# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

kmt = km * 0.15
td = dias * 60
vp = kmt + td

print('Foram rodados {}Km e custou R${:.2f}'.format(km, kmt))
print('O carro foi alugado por {} dias e custou R${:.2f}'.format(dias, td))
print('O valor total que será pago é de R${:.2f}'.format(vp))