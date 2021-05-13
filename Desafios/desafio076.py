compras = ('Pão', 1.5, 'Leite', 3, 'Queijo', 12, 'Bolo', 25, 'Presunto Premiun', 75)
nome = 'Brasil'
print('{:-^40}'.format(nome))
for cont in range(0, len(compras)):
    if type(compras[cont]) == str:
        print(f'{compras[cont]:.<30}', end=' ')
    else:
        print(f'R${compras[cont]:7.2f}')  # EM CASOS DE ALINHAR À ESQUERDA NÃO É NECESSÁRIO O USO DO "<"
print('-'*40)
