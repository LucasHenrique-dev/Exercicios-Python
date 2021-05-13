print('Digite um frase e descubra se ela é um palíndromo')
palav = str(input('Diga a frase: '))
frase = palav.replace(' ', '')
frase1 = ''
for c in range(len(frase)-1, -1, -1):
    frase1 += frase[c]  # poderia ser palav[c] também, só colocar o srtip
print('A palavra de trás pra frente é: \033[34m{}\033[m'.format(frase1.upper()))
if frase1 == frase:
    print('A frase digiada é um palíndromo')
else:
    print('A frase digitada não representa um palíndromo')
# OUTRO JEITO
inverso = frase[::-1]
if inverso == frase:
    print('A frase digitada é um palíndromo')
else:
    print('A frasse digitada não é um palíndromo')
