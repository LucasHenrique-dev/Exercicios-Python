import random
from time import sleep
n1 = random.randint(0, 5)
n2 = int(input('Tente adivinhar o número em que eu pensei, de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if n2 == n1:
    print('-=-'*15)
    print('PARABÉNS, você acertou!!!')
    print('-=-' * 15)
else:
    print('O número em que pensei foi {}, mais sorte da próxima vez'.format(n1))
