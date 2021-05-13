n1 = str(input('Digite seu nome: '))
if n1 == 'lucas':
    print('nome bonito')
elif n1 == 'joao':
    print('Nome comun')
elif n1 in 'ana jessica costa lima':
    print('nome feminino')
else:
    print('bom dia {}'.format(n1))
