def fatorial(num, show=0):
    """
    -> Função que calcula  fatorial de um número dado
        :param num: (Obrigatório)- Indica o número o qual se deseja o fatorial
        :param show: (opcional)- Indica se o usuário deseja ou não ver o cálculo
        :return: O valor do fatorial
    -> Criador: Lucas Henrique
    """
    fat = num
    resp = ''
    for cont in range(num, 0, -1):
        if cont != num:
            fat *= cont
        if show:
            if cont != 1:
                resp += f'{str(cont)} X '
            else:
                resp += f'{str(cont)} = {str(fat)}'
        else:
            resp = fat
    return resp


print(fatorial(12, show=True))
help(fatorial)
