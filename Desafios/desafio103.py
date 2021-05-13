def ficha(nome='<Não informado>', pontos='0'):
    print(f'O jogador {nome} fez {pontos} gol(s) no campeonato')
    print('-'*45)


while True:
    resp = ' '
    jogador = str(input('Digite o nome do jagador: ')).strip().title()
    gols = str(input('Quantos gols fez: ')).strip()
    if jogador == '' and (gols == '' or gols.isalpha()):
        ficha()
    elif gols == '' or gols.isalpha():
        ficha(nome=jogador)
    elif jogador == '':
        ficha(pontos=gols)
    else:
        ficha(jogador, gols)
    while resp not in 'sn':
        resp = str(input('Deseja continuar[S/N]: ')).strip().lower()[0]
    if resp == 'n':
        break
