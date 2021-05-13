n1 = int(input('Digite um número e descubra o seu fatorial: '))
while n1 < 0:
    n1 = int(input('Digite um número positivo, por favor: '))
texto = ''
fat = 1
n2 = n1
'''
while n1 >= 1:
    if n1 == 1:
        texto += str(n1)
    else:
        texto += str(n1) + ' X '
    fat *= n1
    n1 -= 1
'''
for c in range(n1, 0, -1):
    if c == 1:
        texto += str(c)
    else:
        texto += str(c) + ' X '
    fat *= c
if n2 == 0:
    print('0! = 1')
else:
    print('{}! = {} = {}'.format(n2, texto, fat))
