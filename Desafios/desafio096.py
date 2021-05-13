def area(a, b):
    r = a*b
    print('_'*45)
    print(f'O terreno de medidas {a:.2f} m X {b:.2f} m possui área de {r:.2f} m²')


largura = float(input('Informe a largura do terreno: '))
altura = float(input('Infrome a altura do terreno: '))
area(altura, largura)
