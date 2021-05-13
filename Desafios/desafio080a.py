lista = []
for c in range(0, 5):
    valor = int(input('Digite um número: '))
    if len(lista) == 0:
        lista.append(valor)
        print('Valor adicionado à posição 0')
    for pos, info in enumerate(lista):
        if info > valor:
            lista.insert(pos, valor)
            print('Valor adicionado à posição {}'.format(pos))
            break
        elif pos == len(lista)-1 and c != 0:
            lista.append(valor)
            print(f'Valor adicionado à posição {pos+1}')
            break
print(lista)

# JEITO NINJA(PARCIALMENTE COMPLETO- FALHA EM IGUAIS)
lista = []
for c in range(5):
    n = int(input('Número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('O número foi adicionado no final da lista.')
    else:
        for i in range(5):
            if n <= lista[i]:
                lista.insert(i, n)
                print(f'O número foi adicionado na posição {i}.')
                break
print(lista)

# JEITO GUANABARA
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
