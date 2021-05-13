n1 = int(input('Digite a sua primeira nota: '))
n2 = int(input('Digite a sua segunda nota: '))
med = (n1+n2)/2
msg = 'Você passou na matéria'
if med < 7:
    msg = 'Você está na recuperação'
print(f'A sua média é {med} e {msg}')
