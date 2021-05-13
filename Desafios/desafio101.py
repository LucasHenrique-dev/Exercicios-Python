from datetime import date


def voto(ano):
    atual = date.today().year
    if 16 <= atual - ano < 18 or atual - ano >= 65:
        resp = "OPCIONAL"
    elif atual - ano < 65:
        resp = "OBRIGATÓRIO"
    else:
        resp = "NEGATIVO"
    return resp, atual - ano


nasc = int(input('Informe seu ano de nascimento: '))
situacao = voto(nasc)
print(f'Com idade de {situacao[1]} anos o voto é: {situacao[0]}')
