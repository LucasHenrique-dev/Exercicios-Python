primeiro = int(input('Diga o primeiro termo da P.A.: '))
razao = int(input('Diga a razão da P.A.: '))
print('Os 10 primeiros termos da P.A. são: ')
cont = 0
while cont < 10:
    print('{}{}'.format(primeiro, ', ' if cont < 9 else ''), end='')
    primeiro += razao
    cont += 1
