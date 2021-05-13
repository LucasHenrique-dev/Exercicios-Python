from Desafios import moeda

p = float(input('Digite o preço: R$ '))
print(f'''A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}
O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}
Aumentando o valor em 10%, tem-se {moeda.moeda(moeda.aumentar(p, 10))}
Diminuindo o valor em 13%, tem-se {moeda.moeda(moeda.diminuir(p, 13))}''')
