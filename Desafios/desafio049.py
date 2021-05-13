num = int(input('Tabuada, escolha um número para vê-la: '))
for c in range(0, 11):
    print('{:2} X {} = {:2}'.format(c, num, c*num))
