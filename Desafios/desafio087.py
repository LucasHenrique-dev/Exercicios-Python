vetor = []
matriz = []
soma = coluna = 0
for c in range(0, 3):
    for c1 in range(0, 3):
        vetor.append(int(input(f'Informe o valor matriz[{c}][{c1}]: ')))
    matriz.append(vetor[:])
    vetor.clear()
for mat in range(0, 3):
    for mat1 in range(0, 3):
        print(f'{matriz[mat][mat1]:^5}', end=' ')
    print()
for info in matriz:
    for info2 in info:
        if info2 % 2 == 0:
            soma += info2
for cont in range(0, 3):
    coluna += matriz[cont][2]
linha = max(matriz[1])
print(f'''A soma de todos os valores pares digitados é {soma}
A soma dos valores da terceira coluna é {coluna}
O maior valor da segunda linha é {linha}''')
