from random import randint
from time import sleep
from operator import itemgetter
rank = dict()
ranking = dict()
for c in range(0, 4):
    rank['Jogador{}'.format(c+1)] = randint(1, 6)
    print(f'O Jogador{c+1} tirou: {rank["Jogador{}".format(c+1)]}')
    sleep(1)
ranking = sorted(rank.items(), key=itemgetter(1), reverse=True)
print('Ordem dos vencedores:')
for pos, info in enumerate(ranking):
    sleep(1.5)
    print(f'\033[1;3{pos+1}m{pos+1}° lugar:\033[m {info[0]}|\033[1;3{pos+1}m Pontos\033[m -> {info[1]}')
