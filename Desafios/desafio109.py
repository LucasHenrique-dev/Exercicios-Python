from Desafios import moeda

p = float(input('Digite o preço: R$ '))
print(f'''A metade de {moeda.moeda(p)} é {moeda.metade(p)}
O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}
Aumentando o valor em 10%, tem-se {moeda.aumentar(p, 10, False)}
Diminuindo o valor em 13%, tem-se {moeda.diminuir(p, 13, True)}''')
