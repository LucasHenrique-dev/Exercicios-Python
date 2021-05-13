nun = []
while True:
    nun.append(int(input('Digite um valor: ')))
    if nun.count(nun[-1]) > 1:
        print('Esse valor já existe na lista, não irei adicionar-lo')
        nun.pop()
    r = str(input('Deseeja continuar: [S/N] ')).upper().strip()
    if r[0] == 'N':
        break
print('=-' * 30)
print(f'Os valoress digitados foram: {nun}')
nun.sort()
print(f'Em ordem crescente: {nun}')
