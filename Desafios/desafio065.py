resp = ''  # soma = cont = maior = menor = 0
soma = 0
cont = 0
maior = 0
menor = 0
while resp != 'N':
    n1 = int(input('Digite um número: '))
    resp = str(input('Você deseja continuar digitando números[S/N]: ')).strip().upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Resposta inválida, por favor tente novamente[S/N]: ')).strip().upper()
    soma += n1
    if cont == 0:
        maior = n1  # maior = menor = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        elif menor > n1:
            menor = n1
    cont += 1
if maior != menor:
    print(
        'A média {} foi {:.2f}{}'.format('entre os {} valores'.format(cont), soma / cont,
                                         ', já o maior e o menor números foram {} e {}, respectivamente'
                                         .format(maior, menor)))
else:
    print(
        'A média {} foi {:.2f}{}'.format('entre os {} valores'.format(cont) if cont > 1 else 'do único valor digitado',
                                         soma / cont, ' e o valor de maior e menor são coincidentes e iguais a {}'
                                         .format(maior)))
