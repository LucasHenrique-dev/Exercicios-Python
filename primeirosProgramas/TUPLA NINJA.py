tupla = tuple(map(int, input('Informe quatro valores: ').split()))
qtde9 = tupla.count(9)
try:
    posicao_primeiro3 = tupla.index(3)
    print(f'A posição do primeiro 3 foi {posicao_primeiro3}')
except ValueError:
    print('Não foi encontrado nenhum número 3')
pares = tuple(filter(lambda x: x % 2 == 0, tupla))
if qtde9 == 1:
    print('Foi encontrado 1 número 9')
else:
    print(f'Foram encontrados {qtde9} números 9')
if len(pares) == 1:
    print('Foi encontrado 1 valor par')
else:
    print(f'Foram encontrados {len(pares)} valores pares')
