texto = 'EDIÇÃO GAMER'
utensilho = '_'

print('Alinhamneto à direita: {:{}>20}'.format(texto, utensilho))  # O NÚMERO CONTA COM A INFORMAÇÃO DO TEXTO TAMBÉM
print('Alinhamento a esquerda: {:{}<20}'.format(texto, '='))
print('Alinhamento central: {:{}^20}'.format(texto, '*'))
print(f'Alinhamento à direita: {texto:.<20}')
print(f'Alinhamento a esquerda: {texto:>20}')
print(f'Alinhamneto central: {texto:>^20}')
