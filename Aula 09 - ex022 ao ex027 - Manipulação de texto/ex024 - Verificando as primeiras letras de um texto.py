# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cid = str(input('Em que cidade você nasceu? ').strip())
cidade = cid.upper().split()

print('Possui SANTO no inicio do nome da cidade?','SANTO' in cidade[0])