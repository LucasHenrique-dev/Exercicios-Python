from time import sleep
from random import randint
cartoes = int(input('\033[1;31mBem Vindo\033[m, Qunatos cartões da \033[1;34mMEGA SENA\033[m você quer: '))
jogada = []
total = []
numero = 0
for c in range(0, cartoes):
    for cont in range(0, 6):
        numero = randint(1, 60)
        while numero in jogada:
            numero = randint(1, 60)
        jogada.append(numero)
    total.append(jogada[:])
    jogada.clear()
for pos, info in enumerate(total):
    print(f'Jogada número {pos+1}°: {info}')
    sleep(1)
print('\033[1;35mBoa Sorte\033[m nas apostas!!!')
