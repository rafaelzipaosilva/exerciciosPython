# Condições: dois ou mais caminhos que o código pode seguir

# Estrutura condicional:

# se carro.esquerda()   if carro.esquerda():
#    bloco _V_              bloco True
# senão                 else:
#    bloco _F_              bloco False

# Estrutura inteira
tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--FIM--')

# Estrutura simplificada
tempo = int(input('\nQuantos anos tem seu carro? '))
print('Carro Novo' if tempo <= 3 else 'Carro Velho')
# ('bloco True' if 'condição' else 'bloco False')
print('--FIM--')

n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS')
