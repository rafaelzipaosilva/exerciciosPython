# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('ATLÉTICO-MG', 'FLAMENGO', 'PALMEIRAS', 'FORTALEZA', 'CORINTHIANS', 'RED BULL BRAGANTINO', 'FLUMINENSE', 'AMÉRICA-MG', 'ATLÉTICO-GO', 'SANTOS', 'CEARÁ', 'INTERNACIONAL', 'SÃO PAULO', 'ATHLETICO', 'CUIABÁ', 'JUVENTUDE', 'GRÊMIO', 'BAHIA', 'SPORT', 'CHAPECOENSE')
print('-=' * 15)
print(f'Lisa de times: {times}')
print('-=' * 15)

# a: cinco primeiros times
print(f'Os cinco primeiros colocados do Brasileirão: {times[0:5]}')
print('-=' * 15)
# b: quatro últimos colocados
print(f'Os quatro últimos colocados do Brasileirão: {times[-4:]}')
print('-=' * 15)
# c: times em ordem alfabética
print(f'Times do campeonato em ordem alfabética {sorted(times)}')
print('-=' * 15)
# d: posição da chapecoense
print(f'A Chapecoense está na {times.index("CHAPECOENSE") + 1}ª posição')

