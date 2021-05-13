print('''Programa de cadastro, por favor insira os seguinte dados:
-> IDADE
-> SEXO ('M' de masculino e 'F' de femenino)\n''')
maior = homens = mulheres = 0
while True:
    idade = int(input('Informe a sua idade: '))
    while idade <= 0:
        idade = int(input('Valor inválido, por favor digite outro: '))
    sexo = str(input('Informe seu sexo[M/F]: ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Opção inválida, por favor digite outra[M/F]: ')).strip().upper()
    if sexo == 'M':
        homens += 1
    else:
        if idade < 20:
            mulheres += 1
    if idade > 18:
        maior += 1
    resp = str(input('\nVocê deseja continuar[S/N]: \n')).strip().upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Opção inválida, por favor digite outra[S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('Programa encerrado, os resultados dos cadastros foram:\n ')
print(f'''Maiores de 18 anos: {maior}
Quantidade de homens cadastrados: {homens}
Mulheres com menos de 20 anos cadastradas: {mulheres}''')
