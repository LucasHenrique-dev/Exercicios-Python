valor = int(input('Bem Vindo ao caixa-eletrônico, quanto desejas sacar (informe um valor inteiro): R$ '))
while valor <= 0:
    valor = int(input('Valor inválido, por favor tente novamente: '))
notas = [50, 20, 10, 1]
cont = 0
rest = valor
cedulas = []
while rest != 0:
    cedulas.append(rest // notas[cont])
    rest %= notas[cont]
    cont += 1
for c in range(len(cedulas)):
    if cedulas[c] != 0:
        print(f'Cédulas de {notas[c]}: {cedulas[c]}')
