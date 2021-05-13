n1 = float(input('Qual a distância da sua viagem: '))
print('Para viagens de até 200 km o preço é de R$ 0,50 por km, para distâncias maiores será cobrado R$ 0,45 por km')
print('Como a sua é de {:.2f}'.format(n1))
# preco = n1 * 0.5 if n1 <= 200 else n1 * 0.45
if 200.0 >= n1 >= 0:
    preco = n1*0.5
    print('O preço total deu R$ {:.2f}'.format(preco))
elif n1 > 200.0:
    preco = n1*0.45
    print('O preço total foi de: R$ {:.2f}'.format(preco))
else:
    print('Valor inválido para uma viagem')
