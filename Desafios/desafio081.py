numeros = []
cont = 0
while True:
    valor = int(input('Digite um valor: '))
    numeros.append(valor)
    cont += 1
    resp = str(input('Você deseja continuar[S/N]: ')).strip().lower()[0]
    while resp != 'n' and resp != 's':
        resp = str(input('Opção inválida, por favor digite outra[S/N]: ')).strip().lower()[0]
    if resp == 'n':
        break
reverso = sorted(numeros, reverse=True)
print(f'''A lista digitada foi {numeros}
A sua forma decrescente é: {reverso}
{"O valor 5 foi digitado {}{}"
      .format('1 vez' if numeros.count(5) == 1 else numeros.count(5), '' if numeros.count(5) == 1 else ' vezes')
if 5 in numeros else "Não há o número 5 na lista"}''')
if numeros.count(5) > 1:
    print('\nNas posições, com base na lista decrescente: ', end='')
for pos, info in enumerate(reverso):
    if numeros.count(5) == 1 and info == 5:
        print('\nNa posição, com base na lista decrescente: {}'.format(pos+1))
    elif info == 5:
        print(pos+1, end=' ')
