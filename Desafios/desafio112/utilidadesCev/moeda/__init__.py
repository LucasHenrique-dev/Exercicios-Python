import math


def dobro(n, form=False):
    r = n * 2
    if form:
        r = moeda(r)
    return r


def metade(n, form=False):
    r = n / 2
    if form:
        r = moeda(r)
    return r


def aumentar(n, taxa, form=False):
    r = n * (1 + (taxa / 100))
    if form:
        r = moeda(r)
    return r


def diminuir(n, taxa, form=False):
    r = n * (1 - (taxa / 100))
    if form:
        r = moeda(r)
    return r


def moeda(info):
    inteiro = math.trunc(info)
    deci = round((info - inteiro) * 100, 2)
    if deci <= 9:
        decimal = '0'+str(math.trunc(deci))
    else:
        decimal = math.trunc(deci)
    return f'R$ {inteiro},{decimal}'


def resumo(din, au, re):
    print('-'*40)
    print(f'{" "*12}RESUMO DO VALOR')
    print('-'*40)
    print(f'{"Preço analisado:":<30}', end='')
    print(f'{moeda(din)}')
    print(f'{"Dobro do preço:":<30}', end='')
    print(f'{dobro(din, True)}')
    print(f'{"Metade do preço:":<30}', end='')
    print(f'{metade(din, True)}')
    print(f'{"Aumento de {}%:".format(au):<30}', end='')
    print(f'{aumentar(din, au, True)}')
    print(f'{"Redução de {}%:".format(re):<30}', end='')
    print(f'{diminuir(din, re, True)}')
    print('-'*40)
