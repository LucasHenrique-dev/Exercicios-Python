numeros = []
for c in range(0, 5):
    valor = int(input('Digite um número: '))
    numeros.append(valor)
maior = max(numeros)
menor = min(numeros)
print('A sua lista foi: {}'.format(numeros))
print('O maior valor foi {} e se encontra nas posições:'.format(maior), end=' ')
for pos, info in enumerate(numeros):
    if info == maior:
        print(pos+1, end=' ')
print('\nO menor valor foi {} e se encontra nas posições:'.format(menor), end=' ')
for pos, info in enumerate(numeros):
    if info == menor:
        print(pos+1, end=' ')
print('\nPrograma finalizado')
