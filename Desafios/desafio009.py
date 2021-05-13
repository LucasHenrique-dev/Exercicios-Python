n1 = int(input('Digite um número e veja qual a sua tabuada: '))
n = 0
print('{} X {:2} = {:2}'.format(n1, 0, n1*n))
while n < 10:
    n += 1
    print('{} X {:2} = {:2}'.format(n1, n, n1*n))
