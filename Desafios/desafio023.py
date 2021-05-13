n1 = int(input('Digite um número de 0 até 9999: '))
while 0 > n1 or n1 > 9999:
    n1 = int(input('Número inválido, porfavor digite outro: '))
unidade = n1 % 10
dezena = (n1 % 100) - unidade
centena = (n1 % 1000) - (unidade + dezena)
print(f'Unidade = {n1%10}')
print(f'Dezena = {dezena//10}')
print(f'Centena = {centena//100}')
print(f'Unidade de Milhar = {n1//1000}')
print('/////////////////////////////////////')
# OUTRO JEITO
unidade2 = n1 // 1 % 10
dezena2 = n1 // 10 % 10
centena2 = n1 // 100 % 10
milhar = n1 // 1000 % 10
print(f'Unidade: {unidade2}')
print(f'Dezena: {dezena2}')
print(f'Centena: {centena2}')
print(f'Milhar: {milhar}')
