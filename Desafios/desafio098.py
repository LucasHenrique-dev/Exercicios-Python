from time import sleep
cor = {'RED': '\033[1;31m', 'LIMPA': '\033[m'}


def contador(inicio, fim, passo):
    if inicio > fim:
        if passo > 0:
            passo *= -1
        elif passo == 0:
            passo = -1
    elif inicio < fim:
        if passo < 0:
            passo *= -1
        elif passo == 0:
            passo = 1
    print(f'Contagem de {inicio} à {fim} com razão {passo}:')
    for cont in range(inicio, fim + passo, passo):
        sleep(0.5)
        if inicio < fim:
            if cont > fim:
                print(f'{fim}', end=' ')
                break
        elif inicio > fim:
            if cont < fim:
                print(f'{fim}', end=' ')
                break
        print(f'{cont}', end=' ')
    sleep(0.5)
    print(f'{cor["RED"]}FIM{cor["LIMPA"]}')
    print('-='*30)


contador(1, 10, 0)
contador(10, 0, 2)
print('Agora monte sua contagem: ')
while True:
    resp = ' '
    i = int(input('Determine o início: '))
    f = int(input('Onde irá encerrar: '))
    p = int(input('Qual a razão: '))
    contador(i, f, p)
    while resp not in 'SN':
        resp = str(input('Deseja fazer outra simulação[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
