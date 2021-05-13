escala = input('Em que escala você vai infromar a temperatura, (Celsius- C, Fahrenheit- F ou Kelvin- K): ')
temp = float(input('Qual a temperatura atual: '))
conversao = input('Para qual escala você quer converter, Celsius(C), Kelvin(K) ou Fahrenheit(F): ')
if escala == conversao:
    temp = temp
elif escala == 'C':
    if conversao == 'K':
        temp += 273
    else:
        temp = (9/5)*temp + 32
elif escala == 'K':
    if conversao == 'C':
        temp -= 273
    else:
        temp -= 273
        temp = (9*temp/5) + 32
elif escala == 'F':
    if conversao == 'C':
        temp = (temp - 32)*(5/9)
    else:
        temp = (temp - 32)*(5/9)
        temp += 273
print('A temperatura informada, após a conversão, ficou {}'.format(temp))
