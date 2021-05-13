from random import randint, sample
numeros = ()
for c in range(0, 5):
    aleatorio = randint(0, 10)
    numeros += (aleatorio,)
print(f'''A tupla é: {numeros}
O maior número é: {max(numeros)}
O menor é: {min(numeros)}''')

# OUTRO JEITO DE SE FAZER
lista = tuple(sample(range(10), 5))
print(lista)

# OUTRO JEITO
a = tuple(randint(1, 10) for i in range(5))
print(a)
