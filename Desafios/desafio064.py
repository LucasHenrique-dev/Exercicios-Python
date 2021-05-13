n1 = 0  # n1 = soma = cont
soma = 0
cont = 0
while n1 != 999:
    n1 = int(input('Digite um número ou 999 para parar o programa: '))
    if n1 != 999:
        cont += 1
        soma += n1
print('Ao todo você digitou {}{} e a soma foi {}'
      .format(cont, ' número' if cont == 1 else ' números', soma))
