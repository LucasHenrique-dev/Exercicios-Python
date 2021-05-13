print('\033[1;34mAnalisador de expressões matemáticas:\033[m')
valido = []
expre = str(input('Digite a expressão: '))
for ch in expre:
    if ch == '(':
        valido.append('(')
    elif ch == ')':
        if len(valido) > 0:
            valido.pop()
        else:
            valido.append(')')
            break
if len(valido) == 0:
    print('Expressão \033[1;32mVÁLIDA\033[m')
else:
    print('Expressão \033[1;31mINVÁLIDA\033[m')
