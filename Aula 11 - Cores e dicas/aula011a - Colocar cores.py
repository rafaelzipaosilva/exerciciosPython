# CORES NO TERMINAL
# ANSI - escape sequence
#\033[style:text:back m]

'''
STYLE (estilo da fonte)     TEXT (cor do texto)     BACK (cor do fundo)
0 None                      30 Preto                40 Preto
1 Bold                      31 Vermelho             41 Vermelho
3 Itálic                    32 Verde                42 Verde
4 Underline                 33 Amarelo              43 Amarelo
7 Negative                  34 Azul                 44 Azul
9 Tachadec                  35 Magenta              45 Magenta
                            36 Ciano                46 Ciano
                            37 Cinza                47 Cinza

'''

a = 2
b = 5
print('Os valores são \033[33m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
print('\n')

nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('\n')

nome = 'Rafael'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[38;40m'}
print('Me chamo {}{}{}!! Prazer em te conhecer!'.format(cores['pretoebranco'], nome, cores['limpa']))