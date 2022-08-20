# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra sua média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print('Nota 1: {:.1f}. \nNota 2: {:.1f}. \nMédia: {:.1f}.'.format(n1, n2, (n1+n2)/2))