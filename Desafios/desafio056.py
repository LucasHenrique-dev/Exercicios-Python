media = 0
maisVelho = ''
maiorIdade = 0
mulheres = 0
homens = 0
print('Cadastre 4 pessoas a seguir, informando o nome, idade e sexo')
for c in range(0, 4):
    print('\nInformações da {}° pessoa'.format(c+1))
    nome = str(input('Diga o seu nome: ')).replace(' ', '').lower()
    idade = int(input('Diga a sua idade: '))
    while idade <= 0:
        idade = int(input('Valor inválido, por favor digite outro: '))
    sexo = str(input('Diga o sexo: ')).replace(' ', '').lower()
    while sexo != 'homem' and sexo != 'mulher':
        print('Opção inválida, por favor escolha entre Homem ou Mulher')
        sexo = str(input('Sexo: ')).replace(' ', '').lower()
    media += idade
    if sexo == 'homem':
        if maiorIdade < idade:
            maiorIdade = idade
            maisVelho = nome
            homens += 1
    else:
        if idade < 20:
            mulheres += 1
print('A média da idade do grupo é {:.2f}{}'
      ' {}'
      .format(media/4, ', o homem mais velho é {} com {} anos'.format(maisVelho, maiorIdade) if homens >= 1 else '',
              'e há {} {} com menos de 20 anos'.format(mulheres, 'mulher' if mulheres == 1 else 'mulheres')
              if mulheres >= 1 else 'e não há mulheres no grupo'))
