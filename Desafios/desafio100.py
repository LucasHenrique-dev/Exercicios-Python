from random import sample
from time import sleep


def somapar(lst1):
    soma = 0
    for info in lst1:
        for info2 in info:
            if info2 % 2 == 0:
                soma += info2
    print(f'\nA soma de todos os valores pares da lista é {soma}')


def sorteio(lst):
    print('Sorteando números...')
    lst.append(sample(range(101), 5))
    for info in lst:
        for info2 in info:
            sleep(1)
            print(info2, end=' ')
    return lst


lista = list()
numeros = sorteio(lista)
somapar(numeros)
