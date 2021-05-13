print('A seguir dê o nome e o preço dos itens comprados por você: ')
total = menor = vale1000 = cont = 0
barato = ''
while True:
    print('-'*40)
    nome = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Qual o preço: R$ '))
    while preco < 0:
        preco = float(input('Valor inválido, por favor digite novamente: '))
    total += preco
    if cont == 0:
        menor = preco
    if menor >= preco:
        menor = preco
        barato = nome
    if preco > 1000:
        vale1000 += 1
    resp = str(input('Você deseja continuar inserindo produtos[S/N]: ')).strip().upper()
    cont += 1
    while resp not in 'SIMNAO':
        resp = str(input('Opção inválida, por favor digite novamente[S/N]: ')).strip().upper()
    if resp in 'NAO':
        break
print('-'*40)
print('Fim do programa, aqui está o resultado das compras:\n')
print(f'''Total gasto: R$ {total:.2f}, na compra de {cont} produtos
Quantos produtos custam mais de R$ 1000: {vale1000}
O produto com menor preço é {barato}''')
