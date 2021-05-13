n1 = int(input('Digite um número: '))
maior = n1
menor = n1
n2 = int(input('Digite outro número: '))
if maior < n2:
    maior = n2
if menor > n2:
    menor = n2
n3 = int(input('Digite o outro número: '))
if maior < n3:
    maior = n3
if menor > n3:
    menor = n3
print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}')
