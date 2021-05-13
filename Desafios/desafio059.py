from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
escolha = 0
while escolha != 5:
    sleep(2)
    print('''\nO que desejas fazer:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] SABER O MAIOR
    [4] DIGITAR NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    escolha = int(input('\nDigite a opção: '))
    while escolha < 1 or escolha > 5:
        escolha = int(input('Opção inválida, por favor escolha outra: '))
    if escolha == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif escolha == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    elif escolha == 3:
        if n1 == n2:
            print('Não há número maior, ambos são iguais')
        else:
            print('Entre {} e {}, o maior número é {}'.format(n1, n2, n1 if n1 > n2 else n2))
    elif escolha == 4:
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
print('Fim do programa, tenha um bom dia!')
