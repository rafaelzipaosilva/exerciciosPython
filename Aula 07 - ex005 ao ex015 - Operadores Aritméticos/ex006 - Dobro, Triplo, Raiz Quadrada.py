# Crie um algoritmo que leia um número e mostra o seu dobro, o seu triplo e raiz quadrada

n = int(input('Digite um número: '))

print('Número digitado: {}. \nDobro: {}. \nTriplo: {}. \nRaiz quadrada: {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))
