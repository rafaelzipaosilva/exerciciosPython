# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

pri = int(input('1º termo: '))
r = int(input('Razão: '))
cont = 0
inicial = 10
controle = 0
while cont < inicial:
    print('{}'.format(pri), end='')
    print(' ¬ ' if cont < (inicial - 1)  else ' ¬ PAUSA', end='')
    pri += r
    cont += 1
    if cont == inicial:
        controle = int(input('\nDeseja ver quantos termos a mais? (Digite 0 para encerrar): '))
        if controle == 0:
            cont = inicial
        else:
            inicial += controle
print('ACABOU. Foram exibidos {} termos da P.A.'.format(cont))
