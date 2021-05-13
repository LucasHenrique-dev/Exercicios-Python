dados = dict()
gols = list()
total = 0
dados['Nome'] = str(input('Informe o nome: ')).strip().title()
partidas = int(input('Quantas partidas jogadas: '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols feitos na {c+1}° partida: ')))
    while gols[-1] < 0:
        gols.pop()
        gols.append(int(input('Valor inválido, tente novamente: ')))
    total += gols[-1]
dados['Gols'] = gols
dados['Total'] = total  # OU SUM(GOLS) QUE JÁ RETORNA A SOMA DE TODOS OS VAlORES DA LISTA
print('-='*30)
print(dados)
print('-='*30)
for key, value in dados.items():
    print('{}: {}'.format('Gols em cada partida' if key == 'Gols' else key, value))
print('-='*30)
for key, value in dados.items():
    if key == 'Nome':
        print(f'O jogador {value} jogou {len(gols)} partidas')
    elif key == 'Gols':
        for pos, info in enumerate(gols):
            print(f'Na partida {pos+1}°, fez {info} {"gol" if info == 1 else "gols"}')
    else:
        print('Ao todo foram {} gols'.format(total))
print('-='*30)
