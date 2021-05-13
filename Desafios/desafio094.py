pessoas = dict()
dados = list()
media = cont = 0
mulheres = list()
posicao = list()
while True:
    pessoas['Nome'] = str(input('Informe o nome: ')).strip().title()
    pessoas['Sexo'] = str(input('Informe o sexo[M/F]: ')).strip().lower()[0]
    while pessoas['Sexo'] not in 'mf':
        pessoas['Sexo'] = str(input('Opção inválida, tente novamente[M/F]: ')).strip().lower()[0]
    pessoas['Idade'] = int(input('Informe a idade: '))
    while pessoas['Idade'] < 0:
        pessoas['Idade'] = int(input('Valor inválido, tente novamnete: '))
    dados.append(pessoas.copy())
    resp = str(input('Deseja continuar[S/N]: ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Opção inválida, tente novamente[S/N]: ')).strip().lower()[0]
    if resp == 'n':
        break
for pessoa in dados:
    for key, value in pessoa.items():
        if key == 'Idade':
            media += value
        elif key == 'Sexo':
            if value == 'f':
                mulheres.append(pessoa['Nome'])
media /= len(dados)
print('-='*30)
print(f'-O grupo possui {len(dados)} pessoas')
print(f'A média de idade é {media:.0f} anos')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'Lista de pessoas que estão com a idade acima da média:')
for pos, info in enumerate(dados):
    for key, value in info.items():
        if key == 'Idade':
            if value > media:
                posicao.append(cont)
    cont += 1
for pos, info in enumerate(dados):
    if pos in posicao:
        for key, dado in info.items():
            print(f'{key}: {dado if type(dado) == int else dado.title()}', end='; ')
        print()
print('-='*30)
