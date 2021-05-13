from time import sleep


def maior(*numeros):
    print('Analisando os valores passados...')
    if len(numeros) > 0:
        for info in numeros:
            sleep(1)
            print(info, end=' ')
        sleep(0.5)
        print(f'\n{"Foram" if len(numeros) != 1 else "foi"} {"analisados" if len(numeros) != 1 else "analisado"}'
              f' {len(numeros)} {"números" if len(numeros) != 1 else "número"} e o maior é {max(numeros)}')
    else:
        sleep(1)
        print('Não foi informado nenhum número, portanto não há como analisar')
    print('-='*40)


maior(1, 2, 50, 20, 4, 2)
maior(1, 2)
maior(100)
maior()
maior(1, 1, 1)
