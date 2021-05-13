primeiro = int(input('Diga o primeiro termo da P.A.: '))
razao = int(input('Diga a razão: '))
print('Os 10 primeiros termos da P.A. são: ')
limit = 10
cont = 0
texto = str(primeiro)
while cont < limit:
    if cont < limit - 1:
        print('{}, '.format(texto), end='')
    elif cont == limit - 1:
        print('{}'.format(texto))
        print('Se você quiser continuar com o programa então digite a quantidade de termos seguinte, caso não, 0')
        limit = int(input('Digite a quantidade de termos: '))
        while limit <= cont+1 and limit != 0:
            limit = int(input('Valor inválido, por favor digite outro (um maior que o atual ou 0 para parar): '))
            if limit == 0:
                break
        if limit == cont+1:
            print('', end=', ')
    primeiro += razao
    texto = str(primeiro)
    cont += 1
