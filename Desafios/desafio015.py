dias = int(input('Por quantos dias você alugou o carro: '))
preco = float(dias*60)
km = int(input('Quantos quilômetros você percorreu: '))
preco += km*0.15
print('Você deve pagar R$ {:.2f} pelo alugel do carro'.format(preco))
