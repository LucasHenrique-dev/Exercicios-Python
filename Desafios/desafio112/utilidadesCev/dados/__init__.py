def texto(num):
    cores = {'Vermelho': '\033[31;1m', 'Azul': '\033[1;34m', 'Limpa': '\033[m'}
    print(f'{cores["Vermelho"]}ERRO! "{cores["Azul"]}{num}{cores["Vermelho"]}" não é um valor válido!{cores["Limpa"]}')


def leiadinheiro(msg):
    while True:
        resp = str(input(msg)).strip()
        resp1 = resp.replace(' ', '')
        resp1 = resp1.replace(',', '.')
        if '.' in resp1:
            cont = 0
            val = True
            for pos, info in enumerate(resp1+' '):
                if cont > 1:
                    texto(resp)
                    break
                if str(info).isalpha():
                    val = False
                    texto(resp)
                    break
                if info in '.':
                    cont += 1
                if info == ' ':
                    if len(resp1) == 1:
                        texto(resp)
                        break
            if cont == 1 and len(resp1) != 1 and val:
                break
        elif resp1.isnumeric():
            break
        else:
            texto(resp)
    return float(resp1)
