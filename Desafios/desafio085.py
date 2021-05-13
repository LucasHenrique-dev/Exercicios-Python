numeros = [[], []]
for c in range(0, 7):
    n1 = int(input(f'Digite o {c+1}° número: '))
    if n1 % 2 == 0:
        numeros[0].append(n1)
    else:
        numeros[1].append(n1)
print(f'''Os números pares digitados foram: {sorted(numeros[0])}
Os números ímpares digitados foram: {sorted(numeros[1])}''')
