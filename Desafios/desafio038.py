n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O\033[31m primeiro valor\033[m é\033[34m maior\033[m')
elif n2 > n1:
    print('O \033[31mSegundo valor\033[m é\033[34m maior\033[m')
else:
    print('\033[31mNão existe\033[m valor maior, os dois são\033[34m iguais\033[m')
