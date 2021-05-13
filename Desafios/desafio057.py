sexo = str(input('Diga qual o seu sexo[M/F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Valor inválido, por favor digite outro[M/F]: ')).strip().upper()
