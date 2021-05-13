numeros = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in numeros:
        print('Este valor já está presente na {}° posição da lista'.format(numeros.index(valor)+1))
    else:
        numeros.append(valor)
    resp = str(input('Deseja continuar[S/N]: ')).strip().lower()[0]
    while resp != 's' and resp != 'n':
        resp = str(input('Resposta inválida, por favor digite novamente[S/N]: ')).strip().lower()[0]
    if resp == 'n':
        break
print(f'A sua lista em ordem crescente é: {sorted(numeros)}')
