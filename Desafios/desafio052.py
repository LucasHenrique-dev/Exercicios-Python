n1 = int(input('Digite um número e saiba se ele é primo: '))
while n1 <= 0:
    n1 = int(input('Valor inválido, por favor digite outro: '))
cont = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        cont += 1
        if c == n1:
            print('\033[33m {}\033[m'.format(c))
        else:
            print('\033[33m {}\033[m'.format(c), end=',')
    else:
        print('\033[31m {}\033[m'.format(c), end=',')
if cont == 2:
    print('O número \033[34m{}\033[m é primo'.format(n1))
else:
    print('O número \033[32m{}\033[m não é primo'.format(n1))
