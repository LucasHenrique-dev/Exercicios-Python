n1 = float(input('Qual o preço do produto: '))
print('\nNós oferecemos as seguintes opções de pagamento:\n'
      'dinheiro ou cheque confere 10% de desconto\n'
      'à vista no cartão é aplicado 5% de desconto\n'
      '2x no cartão é cobrado o preço do produto sem descontos\n'
      '3x ou mais é aplicado um juros de 20%\n')
condicao = str(input('Como você vai pagar: ')).strip().lower()
if condicao in 'dinheiro cheque':
    print('Compra feita, total a ser pago: R${:.2f}'.format(n1*0.9))
elif '-' in condicao:
    print('Forma de pagamento inválida')
elif '2x' in condicao:
    print('Compra feita, total a ser pago: R${:.2f}'.format(n1))
elif 'x' in condicao:
    print('Compra feita, total a ser pago: R${:.2f}'.format(n1*1.20))
elif 'cartão' in condicao:
    print('Compra feita, total a ser pago: R${:.2f}'.format(n1*0.95))
else:
    print('Forma de pagamento inválida')
