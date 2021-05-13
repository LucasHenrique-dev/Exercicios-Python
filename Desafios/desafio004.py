tecla = input('Digite algo: ')
print('{} possui as seguintes informações:'
      'É AlfaNumérico: {},'
      ' É um texto: {},'
      ' É decimal: {},'
      ' É um dígito: {},'
      ' É um título: {}'
      .format(tecla, tecla.isalnum(), tecla.isalpha(), tecla.isdecimal(), tecla.isdigit(), tecla.istitle()))

