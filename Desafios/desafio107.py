from Desafios import moeda

p = float(input('Digite o preço: R$ '))
print(f'''A metade de {p} é {moeda.metade(p)}
O dobro de {p} é {moeda.dobro(p)}
Aumentando o valor em 10%, tem-se {moeda.aumentar(p, 10):.2f}
Diminuindo o valor em 13%, tem-se {moeda.diminuir(p, 13):.2f}''')
