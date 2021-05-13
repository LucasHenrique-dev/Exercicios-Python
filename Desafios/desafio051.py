n1 = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Qual a razão: '))
print('Os 10 primeiros termos dessa P.A. são: ')
termo = n1+razao
print('{},'.format(n1), end=' ')
for c in range(0, 9):
    if c < 8:
        print('{}, '.format(termo), end='')
    else:
        print(termo)
    termo += razao
