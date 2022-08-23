# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n = input('Digite algo: ')
print('Tipo de dado primitivo:', type(n))

print('É numérico? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('Só tem espaços? ', n.isspace())
print('É alfanumérico? ', n.isalnum())
print('Está em minusculas? ', n.islower())
print('Está em maiúsculas? ', n.isupper())
print('Está capitalizada? (com a primeira letra maiúscula ', n.istitle())