def mensagem(erro):
    cores = {'Vermelho': '\033[1;31m', 'Azul': '\033[1;34m', 'Limpa': '\033[m'}
    print(f'{cores["Vermelho"]}Erro "{cores["Azul"]}{erro.__class__}{cores["Limpa"]}{cores["Vermelho"]}",'
          f' tente novamente{cores["Limpa"]}')


def leiaint(info):
    while True:
        try:
            num = int(input(info))
        except Exception as erro:
            mensagem(erro)
        else:
            break

    return num


def leiafloat(info):
    while True:
        try:
            num = float(input(info))
        except Exception as erro:
            mensagem(erro)
        else:
            break
    return num


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print('O número inteiro digitado foi {} e o real foi {}'.format(n1, n2))
