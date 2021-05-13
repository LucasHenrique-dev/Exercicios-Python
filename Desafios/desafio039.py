from datetime import date

n1 = int(input('Diga em que ano você nasceu: '))
anoAtual = date.today().year
idade = anoAtual - n1
if idade == 18:
    print('\033[31mAtenção\033[m Você deve se \033[34malistar\033[m esse ano')
elif idade < 18:
    print('Você ainda \033[33mnão deverá\033[m se \033[34malistar\033[m, apenas daqui a {} {}'
          .format(18-idade, 'ano' if 18-idade == 1 else 'anos'))
else:
    print('Você \033[32mjá passou\033[m da idade de se \033[34malistar\033[m a {} {}'
          .format(idade-18, 'ano' if idade-18 == 1 else 'anos'))
