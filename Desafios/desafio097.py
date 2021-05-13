def escreva(texto):
    tam = len(texto) + 2
    print('~' * tam)
    print(f' {texto}')
    print('~' * tam)


while True:
    resp = ' '
    frase = str(input('O que você quer escrever: ')).strip()
    escreva(frase)
    while resp not in 'sn':
        resp = str(input('Deseja continuar[S/N]: ')).strip().lower()
    if resp == 'n':
        break
