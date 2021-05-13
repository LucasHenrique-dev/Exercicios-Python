n1 = float(input('Informe a velocidade do carro: '))
print('O limite de velocidade é 80 km/h e a sua velocidade foi de {:.2f} km/h'.format(n1))
if n1 > 80.0:
    multa = (n1 - 80.0)*7
    print('Você excedeu o limite e agora deve pagar um multa de: R$ {:.2f}'.format(multa))
else:
    print('Continue dirigindo com segurança')
