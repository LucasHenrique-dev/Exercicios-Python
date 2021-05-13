numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    escolha = int(input('Digite um número de 0 a 20: '))
    while escolha < 0 or escolha > 20:
        escolha = int(input('Número inválido, por favor digite outro: '))
    print('-'*30)
    print(f'Você digitou o número {numeros[escolha]}')
    print('-'*30)
    opcao = str(input('Deseja continuar[S/N]: ')).strip().lower()[0]
    while opcao != 's' and opcao != 'n':
        opcao = str(input('Opção inválida, por favor tente novamente[S/N]: ')).strip().lower()[0]
    if opcao == 'n':
        break
print('Programa finalizado com sucesso!')
