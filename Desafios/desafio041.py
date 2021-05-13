from datetime import date
anoAtual = date.today().year
n1 = int(input('Em que ano você nasceu: '))
while n1 < 0 or n1 > anoAtual:
    n1 = int(input('Valor inválido, por favor digite outro: '))
idade = anoAtual - n1
if idade <= 9:
    print('Você se enquadra na categoria \033[1;34mMIRIN\033[m de natação')
elif idade <= 14:
    print('Você se enquadra na categoria \033[1;34mINFANTIL\033[m de natação')
elif idade <= 19:
    print('Você se enquadra na categoria \033[1;34mJÚNIOR\033[m de natação')
elif idade <= 20:
    print('Você se enquadra na categoria \033[1;34mSÊNIOR\033[m de natação')
else:
    print('Você se enquadra na categoria \033[1;34mMASTER\033[m de natação')
