from random import randint

print('''Vamos jogar par ou ímpar, você dâ um número (entre 0 e 10) e escolhe 
\033[1;32mPAR\033[m ou \033[1;31mÍMPAR\033[m, dependendo do que eu jogar você pode ganhar se a soma der o escolhido
e perder caso contrário. Quantas vezes será que \033[33mvocê\033[m consegue se manter \033[1;34mINVICTO!\033[m''')
cont = 0
while True:
    jogador = int(input('\nQual a sua jogada: '))
    while jogador > 10 or jogador < 0:
        jogador = int(input('Jogada inválida, por favor tente novamente: '))
    computador = randint(0, 10)
    soma = 0
    escolha = str(input('Qual será sua escolha[P/I]: ')).strip().upper()[0]
    while escolha != 'P' and escolha != 'I' and escolha != 'Í':
        escolha = str(input('Opção inválida, por favor tente novamente[P/I]: ')).strip().upper()[0]
    soma = jogador + computador
    print('Eu escolhi {}, logo a soma resulta em: {}'.format(computador, soma))
    if escolha == 'P':
        if soma % 2 == 0:
            cont += 1
            print('\033[1;34mPARABÉNS\033[m você venceu, hora do {}° round'.format(cont + 1))
        else:
            print('Você \033[1;31mPERDEU\033[m, mais sorte da próxima vez')
            break
    else:
        if soma % 2 == 1:
            cont += 1
            print(f'\033[1;34mPARABÉNS\033[m você venceu, hora do {cont+1}° round')
        else:
            print('Você \033[1;31mPERDEU\033[m, mais sorte da próxima vez')
            break
if cont >= 10:
    print(f'\n\033[1;34mINCRÍVEL\033[m você consegui me vencer \033[1;35m{cont}\033[m vezes!!!')
else:
    print(f'\nResultado final: Você conseguiu vencer {cont} {"vez" if cont == 1 else "vezes"}')
