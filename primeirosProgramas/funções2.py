def soma(z, x, y=1):
    """
    Funçao responsável por somar números
    :param z: primeiro termo da soma
    :param x: segundo termo da soma
    :param y: opcinal e indica um dos termos da soma
    :return: não possui
    """
    s = z + x + y
    print(f'A soma vale {s}')


soma(1, 2, 3)
soma(5, 4)
soma(1, 3)


def teste(b):
    global a
    a += 6
    b += 5
    print(f'O valor de "a" é {a}\n'
          f'O valor de "b" é {b}')


a = 4
print(f'O valor da "a" antes da chamada da função {a}')
teste(a)
print(f'A variável "a" vale {a}')

