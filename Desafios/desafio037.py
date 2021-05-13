n1 = int(input('Escreva um número: '))
print('Para qual base você quer ver esse número: \n'
      '(1)- BINÁRIO\n'
      '(2)- OCTAL\n'
      '(3)- HEXADECIMAL\n')
escolha = int(input('Qual o que você quer: '))
if escolha == 1:
    print('O número {}, representado em binário fica: {}'.format(n1, bin(n1)[2:]))
elif escolha == 2:
    print(f'O número {n1} escrito em Octal é {oct(n1)[2:]}')
elif escolha == 3:
    print(f'O número {n1} representado na base Hexadecimal é {hex(n1)[2:]}')
else:
    print('Opção inválida de escolha')
