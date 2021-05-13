numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = str(input('Você deseja continuar[S/N]: ')).strip().lower()[0]
    while resp != 'n' and resp != 's':
        resp = str(input('Opção inválida, por favor digite outra[S/N]: ')).strip().lower()[0]
    if resp == 'n':
        break
for info in numeros:
    if info % 2 == 0:
        pares.append(info)
    else:
        impares.append(info)
print(f'''A lista digitada foi: {numeros}
{"A lista com números pares: " if len(pares) > 0 else "Não houveram números pares"}{pares if len(pares) > 0 else ""}
{"A lista com números ímpares: "if len(impares)>0else"Não houveram números ímpares"}{impares if len(impares)>0 else ""}
''')
