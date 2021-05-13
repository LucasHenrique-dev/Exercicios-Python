def notas(*numeros, sit=False):
    """
        ->Função que mostra um panorama das notas de uma turma (situação- OPCIONAL)
    :param numeros: (OBRIGATÓRIO) Notas da turma
    :param sit: (OPCIONAL) situação da turma, entre "BOA"(>=7), "MEDIANA"(<=7 e >=5) e "RUIM"(<=5)
    :return: retorna um dicionário com todas as informações solicitadas
    """
    info = dict()
    info['Total'] = len(numeros)
    info['Maior'] = max(numeros)
    info['Menor'] = min(numeros)
    info['Media'] = sum(numeros)/info['Total']
    if sit:
        if info['Media'] >= 7:
            info['Situação'] = 'Boa'
        elif info['Media'] >= 5:
            info['Situação'] = 'Mediana'
        else:
            info['Situação'] = 'Ruim'
    return info


n = notas(0.5, 10, 0.6, 8, sit=True)
print(n)
help(notas)
