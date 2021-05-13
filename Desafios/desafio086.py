matriz = []
for c in range(0, 3):
    for c1 in range(0, 3):
        matriz.append(int(input(f'Matriz[{c}][{c1}]: ')))
for c2 in range(0, 9):
    if c2 % 3 == 0 and c2 != 0:
        print('')
    print(f'{matriz[c2]:^5}', end=' ')
