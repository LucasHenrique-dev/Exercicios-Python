print('Dê o valor de 7 pesos e descubra o maior e o menor entre eles')
peso = float(input('Digite o valor do 1° peso: '))
while peso <= 0:
    peso = float(input('Valor inválido, por favor digite outro: '))
maior = peso
menor = peso
for c in range(0, 6):
    peso = float(input('Digite o {}° peso: '.format(c+2)))
    while peso <= 0:
        peso = float(input('Valor inválido, por favor digite outro: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
if maior == menor:
    print('Todos os 7 pesos foram iguais, portanto não há maior e nem menor')
else:
    print('O maior peso foi de {:.2f}kg e o menor foi de {:.2f}kg'.format(maior, menor))
