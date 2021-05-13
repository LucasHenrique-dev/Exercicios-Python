numeros = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    numeros.append(valor)
    for cont in range(len(numeros)-1, 0, -1):
        if numeros[cont] < numeros[cont-1]:
            aux = numeros[cont]
            numeros[cont] = numeros[cont-1]
            numeros[cont-1] = aux
print(f'A sua lista em ordem crescente é: {numeros}')
