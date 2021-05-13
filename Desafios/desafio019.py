from random import choice
n1 = input('Diga o nome do primeiro aluno: ')
n2 = input('Diga o nome do segundo aluno: ')
n3 = input('Diga o nome do terceiro aluno: ')
n4 = input('Diga o nome do quarto aluno: ')
'''''
escolha = random.randint(1, 4)
if escolha == 1:
    print('O aluno {} foi escolhido para apagar o quadro'.format(n1))
elif escolha == 2:
    print('O aluno {} foi escolhido para apagar o quadro'.format(n2))
elif escolha == 3:
    print('O aluno {} foi escolhido para apagar o quadro'.format(n3))
elif escolha == 4:
    print(f'O aluno {n4} foi escolhido para apagar o quadro')
'''
lista = [n1, n2, n3, n4]
escolha = choice(lista)
print(f'O aluno escolhido para apagar o quadro é {escolha}')
