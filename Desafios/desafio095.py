dados = dict()
cores = {'Amarelo': '\033[33m', 'Limpa': '\033[m'}
jogadores = list()
partidas = 0
gols = list()
while True:
    dados['Nome'] = str(input('Informe o nome: ')).strip().title()
    partidas = int(input('Informe o número de partidas jogadas por {}: '.format(dados['Nome'])))
    while partidas < 0:
        partidas = int(input('Valor inválido, tente novamente: '))
    for c in range(0, partidas):
        gols.append(int(input('Número de gols feito na {}° partida: '.format(c + 1))))
        while gols[-1] < 0:
            gols.pop()
            gols.append(int(input('Valor inválido, tente novamente: ')))
    dados['Gols'] = gols[:]
    gols.clear()
    resp = str(input('Deseja continuar[S/N]: ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Opção inválida, tente novamente[S/N]: ')).strip().lower()[0]
    jogadores.append(dados.copy())
    if resp == 'n':
        break
print(f'{cores["Amarelo"]}-={cores["Limpa"]}' * 33)
print(f'{"CÓDIGO":<16}{"JOGADOR":<17}{"GOLS":<25}{"TOTAL"}')
for pos, info in enumerate(jogadores):
    print(f'{pos:<16}', end='')
    for value in info.values():
        if type(value) == list:
            print(f'{str(value):<25}', end='')  # SE O PROBLEMA É NÃO SER STRING, ENTÃO QUE SEJA
        else:
            print(f'{value:<17}', end='')
    print(sum(value))
print(f'{cores["Amarelo"]}-={cores["Limpa"]}' * 33)
while True:
    resp = str(input(f'Você deseja saber mais sobre algum jogador[S/N]: ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Opção inválida, tente novamente[S/N]: ')).strip().lower()[0]
    if resp == 'n':
        break
    escolha = int(input('Qual o código: '))
    while escolha < 0 or escolha > len(jogadores) - 1:
        escolha = int(input('Opção inválida, tente novamente: '))
    for pos2, info2 in enumerate(jogadores):
        if pos2 == escolha:
            for value in info2.values():
                if type(value) == str:
                    print('{}{:{}^35}{}'
                          .format(cores['Amarelo'], 'INFORMAÇÕES DO JOGADOR(A)-> {}'.format(value.upper()), '-',
                                  cores['Limpa']))
                elif type(value) == list:
                    for pos3, gol in enumerate(value):
                        print(f'Na {pos3 + 1}° partida, fez {gol}{" gol" if gol == 1 else " gols"}')
print(f'{cores["Amarelo"]}-={cores["Limpa"]}' * 33)
