from random import randint
from time import sleep
print('Irei pensar em um número entre 0 e 10: ')
print('Pensando...')
sleep(1.5)
computador = randint(0, 10)
cont = 0
jogador = int(input('Pronto agora que pensei, tente adivinhar: '))
while jogador != computador:
    jogador = int(input('Maior... tente novamente: ' if computador > jogador else 'Menor... tente novamente: '))
    cont += 1
print('Você consegui adivinhar {}{}'
      .format('após {}'.format(cont+1) if cont > 0 else '',
              ' tentativas' if cont > 0 else 'de primeira, \033[1;34mPARABÉNS\033[m!!!'))
