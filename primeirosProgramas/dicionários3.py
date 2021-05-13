cor = {'Azul': '\033[34m', 'Limpa': '\033[m'}
print(f'{cor["Azul"]} olá{cor["Limpa"]} pessoal')
lista = [{'Nome': 'Lucas', 'Casa': 'Apartamento'}, {'Camisa': 'Amarela estampada'}]
for info in lista[0].values():
    print(info)
