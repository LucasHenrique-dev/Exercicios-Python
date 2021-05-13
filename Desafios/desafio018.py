import math
n1 = float(input('Informe um ângulo: '))
ang = math.radians(n1)
print(f'O ângulo {n1} possui:\n'
      f' seno = {math.sin(ang):.2f}\n'
      f' cosseno = {math.cos(ang):.2f}\n'
      f' tangente = {math.tan(ang):.2f}')
