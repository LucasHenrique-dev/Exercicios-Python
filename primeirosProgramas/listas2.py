numeros = [3, 2, 32, 0, 1, 43, 22, 2]
print(numeros)
ordenado = sorted(numeros)
reverso = sorted(numeros, reverse=True)
# numeros.sort() ORDENA A LISTA E NÃO RETORNA NADA
# numeros.sort(reverse=True)  # TRANSFORMA A LISTA ORIGINAL EM UM REVERSA E NÃO RETORNA NADA
print(ordenado)
print(reverso)
numeros.insert(1, 4)
print(numeros)
numeros.pop()  # ELIMINA A INFORMAÇÃO DESEJADA OU SE NÃO INFORMADA O ÚLTIMO
print(numeros)
del numeros[2]
print(numeros)
numeros.append(4)
numeros.remove(4)
print(numeros)
for pos, info in enumerate(numeros):
    print(f'Na posição {pos} encontrasse o valor {info}')
numeros2 = numeros  # É REALIZADO UMA LIGAÇÃO E NÃO UMA CÓPIA, O QUE ACONTECE EM UMA AFETA A OUTRA
numeros3 = numeros[:]  # REALIZAÇÃO DE UMA CÓPIA, AGORA ELES SÃO INDEPENDENTES
print('-'*35)
print(f'''Lista A: {numeros}
Lista B: {numeros2}
Lista C: {numeros3}''')
numeros2[2] = 100
numeros3[2] = 50
print('-'*35)
print(f'''Lista A: {numeros}
Lista B: {numeros2}
Lista C: {numeros3}''')
