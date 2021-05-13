import math
n1 = int(input('Qual o valor do cateto Oposto: '))
n2 = int(input('Qual o valor do catteto adjacente: '))
s = n1 ** 2 + n2 ** 2
h = math.sqrt(s)
print(f'O triângulo retângulo de catetos {n1} e {n2} possui como hipotenusa {h}')
