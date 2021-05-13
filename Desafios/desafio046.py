from time import sleep
import emoji
print('Vai começar o estouro dos fogos de artifício, atenção a contagem regressiva:')
sleep(3)
for c in range(11, 0, -1):
    print(c-1)
    sleep(1)
print()
for c1 in range(0, 3):
    print(emoji.emojize(':fireworks:', use_aliases=True), end='')
print('\nBOAS FESTAS!!!')
