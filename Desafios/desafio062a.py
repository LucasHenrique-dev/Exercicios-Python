primeiro = int(input('Diga o primeiro termo da P.A.: '))
razao = int(input('A razão agora: '))
cont = 0
limit = 10
termos = 0
print('Os 10 primeiros termos são: ')
while cont < limit:
    if cont < limit-1:
        print('{} -> '.format(primeiro), end='')
    else:
        print('{} -> Fim dos {} termos'.format(primeiro, cont+1))
    if cont == limit-1:
        termos = int(input('Você deseja ver mais quantos termos (0 encerra): '))
        while limit < 0:
            termos = int(input('Valor inválido, por favor digite novamente: '))
        limit += termos
    primeiro += razao
    cont += 1
print('Programa finalizado, tenha um bom dia!')
