try:
    n = str(input('Digite algo: '))
except KeyboardInterrupt:
    print('Este comando não funciona mais!!!!')  # DORIME
else:
    print('Você digitou {}'.format(n))
