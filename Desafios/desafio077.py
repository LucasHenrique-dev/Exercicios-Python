tupla = ('livro', 'caderno', 'lapis', 'borracha', 'caneta')
vogais = ('a', 'e', 'i', 'o', 'u')
for c in tupla:
    print(f'\nPara a palavra {c}, Há vogais: ', end='')
    for vog in vogais:
        if vog in c:
            print(f'{vog}', end=' ')
print('\nFIM')
