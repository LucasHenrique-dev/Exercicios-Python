from datetime import date
n1 = int(input('Digite o ano ou "0" para analisar o atual: '))
if n1 == 0:
    n1 = date.today().year
if n1 % 4 == 0:
    if n1 % 100 == 0:
        if n1 % 400 == 0:
            print('O ano {} é bissexto'.format(n1))
        else:
            print('O ano {} não é bissexto'.format(n1))
    else:
        print(f'O ano {n1} é bissexto')
else:
    print(f'O ano {n1} não é bissexto')
