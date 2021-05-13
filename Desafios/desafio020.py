from random import sample, shuffle
n1 = input('Diga o nome do primeiro aluno: ')
n2 = input('Diga o nome do segundo aluno: ')
n3 = input('Diga o nome do terceiro aluno: ')
n4 = input('Diga o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação dos alunos é {}'.format(lista))
ordem = sample(lista, k=1)
print(f'Uma outra forma é {ordem}')
'''''
esc1 = choice(lista)
esc2 = choice(lista)
while esc2 == esc1:
    esc2 = choice(lista)
esc3 = choice(lista)
while esc3 == esc2 or esc3 == esc1:
    esc3 = choice(lista)
esc4 = choice(lista)
while esc4 == esc1 or esc4 == esc2 or esc4 == esc3:
    esc4 = choice(lista)
print('A ordem de apresentação dos trabalhos é: \n'
      f'Primeiro = {esc1} \n'
      f'Segundo = {esc2} \n'
      f'Terceiro = {esc3} \n'
      f'Quarto = {esc4} \n')
'''''
