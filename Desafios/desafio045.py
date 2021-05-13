from random import choice
from time import sleep

print('Vamos jogar \033[32mJokenpô\033[m')
escolhas = ['pedra', 'papel', 'tesoura']
computador = choice(escolhas)
jogador = str(input('Já escolhi a minha opção, qual a sua jogador \033[34mdesafiante\033[m: ')).strip().lower()
while not (jogador in escolhas):
    jogador = str(input('opção invalida, por favor digite outra: ')).strip().lower()
print('Jogada contabilizada, hora de saber o vencedor')
sleep(1.5)
print('\033[34mJo\033[m...')
sleep(1)
print('\033[34mKen\033[m...')
sleep(1)
print('\033[34mPô\033[m!!!')
sleep(2)
print('\033[1;31mComputador\033[m: \033[1;35m{}\033[m'.format(computador))
print('\033[1;32mJogador\033[m: \033[1;36m{}\033[m'.format(jogador))
if computador == jogador:
    print('\033[1;33mEMPATE\033[m')
elif computador == 'pedra':
    if jogador == 'tesoura':
        print('Vitória do \033[1;31mCOMPUTADOR\033[m')
    else:
        print('Vitória do \033[1;34mJOGADOR DESAFIANTE\033[m')
elif computador == 'papel':
    if jogador == 'tesoura':
        print('Vitória do \033[1;34mJOGADOR DESAFIANTE\033[m')
    else:
        print('Vitória do \033[1;31mCOMPUTADOR\033[m')
elif computador == 'tesoura':
    if jogador == 'pedra':
        print('Vitória do \033[1;34mJOGADOR DESAFIANTE\033[m')
    else:
        print('Vitória do \033[31mCOMPUTADOR\033[m')
