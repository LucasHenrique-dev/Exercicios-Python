from datetime import date
print('Diga-me o ano de nascimento de 7 pessoas e eu direi quantos há de maioridade')
atual = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input('Ano de nascimento da {}ª pessoa: '.format(c+1)))
    while ano <= 0 or ano > atual:
        ano = int(input('Ano inválido, por favor digite outro: '))
    if atual - ano >= 18:
        maior += 1
    else:
        menor += 1
print("""\nMaioridade: {}
Menoridade: {}
""".format(maior, menor))
