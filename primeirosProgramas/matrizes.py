vetor = list()
matriz = list()
for c in range(0, 3):
    for c1 in range(0, 3):
        vetor.append(int(input('Digite um valor: ')))
    matriz.append(vetor[:])
    vetor.clear()
teste = []
teste.append([int(input('Número: ')), str(input('Nome: '))])
print(teste)

