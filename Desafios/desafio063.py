n1 = int(input('Digite o número de termos da sequência de fibonacci que você quer ver: '))
while n1 <= 0:
    n1 = int(input('Valor inválido, por favor digite outro: '))
if n1 == 1:
    print('0')
elif n1 == 2:
    print('0 -> 1')
else:
    print('0 -> 1 ', end='-> ')
cont = 0
aux1 = 1
aux2 = 1
fib = 1
while cont < n1 - 2 and n1 > 2:
    print('{} {}'.format(fib, '' if cont + 1 == n1 - 2 else '-> '), end='')
    fib = aux1 + aux2
    aux2 = aux1
    aux1 = fib
    cont += 1
# JEITO NIJA\\\\\\\\\\\\\\\\\\\\\\\
print()
n = int(input("numero: "))
lista = [0, 1]
for i in range(n - 2):
    lista.append(lista[-1] + lista[-2])
print(lista)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# MAIS 1 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print()
n = int(input('Escreva quantos números quer da Sequência de Fibonacci: '))
fibon = [0, 1]
for c in range(0, n):
    fibon.append(fibon[c] + fibon[c + 1])
print(fibon[:n])
#  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
