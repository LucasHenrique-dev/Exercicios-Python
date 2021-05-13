numeros = ()
for c in range(0, 4):
    teclado = int(input('Digite um número: '))
    numeros += (teclado,)
if numeros.__contains__(9):  # NÃO É NECESSÁRIO A VERIFICAÇÃO
    print(f'O número 9 apareceu {numeros.count(9)} vezes')
else:
    print('O número 9 não apareceu nenhuma vez')
if numeros.__contains__(3):
    print(f'A primeira aparição do número 3 na tupla é na {numeros.index(3) + 1} posição')
else:
    print('O número 3 não apareceu nenhuma vez')
print(f'Os números pares foram: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(f'{c}', end=' ')
print('\nPrograma finalizado')
