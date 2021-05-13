pessoas = list()
dados = list()
trave = False
while True:
    dados.append(str(input('Digite o nome: ')).strip().title())
    peso = float(input('Digite o peso: '))
    dados.append(peso)
    if not trave:
        maior = menor = peso
        trave = True
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Você deseja continuar[S/N]: ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Opção inválida, por favor tente novamente[S/N]: ')).strip().lower()[0]
    if resp == 'n':
        break
print(f'''Houveram um total de {len(pessoas)} pessoas cadastradas
O maior peso foi de {maior:.2f}Kg, pertencente(s) à:''', end=' ')
for info in pessoas:
    if info[1] == maior:
        print(f'[{info[0]}]', end=' ')
print(f'\nO menor peso foi de {menor:.2f}Kg e pertence à:', end=' ')
for info in pessoas:
    if info[1] == menor:
        print(f'[{info[0]}]', end=' ')
