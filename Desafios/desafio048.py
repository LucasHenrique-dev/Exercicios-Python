soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'Foram encontrados {cont} números ímpares e divisíveis por 3 entre 1 e 500 e seu somatório é {soma}')
