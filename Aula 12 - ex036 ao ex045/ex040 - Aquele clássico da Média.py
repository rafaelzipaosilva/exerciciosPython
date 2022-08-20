# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = float('{:.1f}'.format((n1 + n2) / 2))

if 10.1 > media >= 7.0:
    print('A media do aluno foi {:.1f}.\nALUNO APROVADO'.format(media))
elif 6.9 >= media >= 5.0:
    print('A media do aluno foi {:.1f}.\nALUNO EM RECUPERAÇÃO'.format(media))
elif media < 5.0:
    print('A média do aluno foi {:.1f}.\nALUNO REPROVADO'.format(media))
else:
    print('NOTA INVÁLIDA')