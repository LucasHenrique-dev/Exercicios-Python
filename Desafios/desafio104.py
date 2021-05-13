def leiaint(info):
    while True:
        texto = str(input(info))
        if texto.isdecimal():
            return texto
        else:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
