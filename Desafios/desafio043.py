peso = float(input('Diga qual o seu peso: '))
while peso <= 0:
    peso = float(input('Valor inválido, por favor digite outro: '))
altura = float(input('Diga qual a sua altura: '))
while altura <= 0:
    altura = float(input('Valor inválido, por favor digite outro: '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Você está abaixo do peso, com um IMC de {:.2f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Você possui um peso ideal, com um imc de {:.2f}'.format(imc))
elif 25 <= imc <= 30:
    print('Você está sobrepeso com um imc de{:.2f}'.format(imc))
elif 30 <= imc <= 40:
    print('Você possui obesidade, com um imc de {:.2f}'.format(imc))
elif imc > 40:
    print('Você possui \033[1;31mOBESIDADE MÓRBIDA\033[m com um imc de {:.2f}'.format(imc))
