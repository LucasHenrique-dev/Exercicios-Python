soma = 0
print('A seguir digite 6 números e ao fim será exibido a soma dos números pares')
for c in range(0, 6):
    num = int(input('Digite o {}° número: '.format(c+1)))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares é {}'.format(soma))
