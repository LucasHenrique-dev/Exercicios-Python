while True:
    n1 = int(input('digite um número e veja sua tabuada: '))
    if n1 < 0:
        break
    cont = 0
    print('-'*20)
    while cont <= 10:
        print(f'{n1} X {cont:2} = {n1*cont:2}')
        cont += 1
    print('-'*20)
print('\n\033[1;34mPrograma encerrado\033[m')
