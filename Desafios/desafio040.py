n1 = float(input('Diga a primeira nota: '))
while n1 < 0 or n1 > 10:
    n1 = float(input('Valor inválido, por favor digite outro: '))
n2 = float(input('Diga a segunda nota: '))
while n2 < 0 or n2 > 10:
    n2 = float(input('Valor inválido, por favor digite outro: '))
med = (n1+n2)/2
if med < 5.0:
    print('Sua média foi de \033[32m{:.2f}\033[m e você está \033[1;31mREPROVADO\033[m'.format(med))
elif 5 <= med <= 6.9:
    print('Sua média foi de \033[32m{:.2f}\033[m e você está na \033[1;35mRECUPERAÇÃO\033[m'.format(med))
else:
    print('Sua média foi de \033[32m{:.2f}\033[m e você está \033[1;34mAPROVADO\033[m'.format(med))
