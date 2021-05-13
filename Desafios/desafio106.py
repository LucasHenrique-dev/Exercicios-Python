from time import sleep


def capricho(info, cor):
    sleep(0.5)
    tam = len(info) + 8
    print(f'{cores[cor]}~' * tam)
    print(f'    {info}')
    print('~' * tam)


def ajuda():
    """
      -> Programa de auxílio, orientação e ajuda a respeito das funções e bibliotecas do Python
    :return: Nada
    """
    while True:
        texto = 'Bem vindo ao sistema de ajuda e orientação sobre funções e bibliotecas'
        capricho(texto, cor="Ciano")
        sleep(1)
        resp = str(input('{}Sobre o que você precisa de ajuda(FIM, encerra): '.format(cores['Limpa']))).strip().lower()
        if resp == 'fim':
            sleep(0.5)
            texto = 'Obrigado por utilizar o sistema!'
            capricho(texto, cor="Magenta")
            break
        else:
            texto = f'Acesando o manual do comando: {resp}'
            capricho(texto, cor="Vermelho")
            sleep(1)
            print(f'{cores["Branco"]}{cores["Reverse"]}')
            help(resp)
            print(cores['Limpa'], end='')


cores = {'Vermelho': '\033[1;41m', 'Magenta': '\033[1;45m', 'Branco': '\033[1;30;48m', 'Ciano': '\033[1;46m',
         'Reverse': '\033[7m', 'Limpa': '\033[m'}
ajuda()
