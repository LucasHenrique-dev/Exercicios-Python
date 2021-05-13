n1 = float(input('Digite o comprimento de uma reta: '))
n2 = float(input('Digite a de outra: '))
n3 = float(input('Agora a da última: '))
lista = [n1, n2, n3]
lista.sort()
menor = lista[0]
medio = lista[1]
maior = lista[2]
if maior < (medio + menor) and menor > (maior - medio):
    print('A combinação dessas três retas podem formar um triângulo')
    if maior == menor == medio:
        print('O triângulo formado é equilátero, tem os 3 lados iguais')
    elif maior == menor or menor == medio or maior == medio:
        print('O triângulo formado é isósceles, possui 2 lados iguais')
    else:
        print('O triângulo formado é escaleno, possui os 3 lados diferentes')
else:
    print('A combinação dessas 3 retas não podem formar um triângulo')
print(f'Maior: {maior:.2f}, menor: {menor:.2f} e médio: {medio:.2f}')
