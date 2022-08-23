# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Caneta', 2.9, 'Borracha', 1.7, 'Caderno', 4.99, 'Lápis', 1.7)

print('-' * 40)
print(f'{" PAPELARIA DO IN ":-^40}')

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}R$ {produtos[pos+1]:>5.2f}')
print('-'*40)