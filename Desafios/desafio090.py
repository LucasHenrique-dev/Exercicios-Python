status = dict()
alunos = list()
notas = list()
while True:
    status['Nome'] = str(input('Digite o nome: ')).strip().title()
    for c in range(2):
        notas.append(float(input(f'Digite a {c+1}° nota: ')))
        while notas[-1] < 0 or notas[-1] > 10:
            notas.pop()
            notas.append(float(input('Nota inválida, tente novamente: ')))
    status['Nota'] = notas[:]
    notas.clear()
    status['Média'] = (status['Nota'][0] + status['Nota'][1])/2
    if status['Média'] >= 7:
        status['Situação'] = '\033[1;34mAprovado\033[m'
    elif 3 <= status['Média'] < 7:
        status['Situação'] = '\033[1;33mRecuperação\033[m'
    else:
        status['Situação'] = '\033[1;31mReprovado\033[m'
    resp = str(input('Deseja continuar[S/N]: ')).strip().lower()[0]
    while resp not in 'ns':
        resp = str(input('Opção inválida, tente novamente[S/N]: ')).strip().lower()[0]
    alunos.append(status.copy())
    if resp == 'n':
        break
print(f'{"GRADE":{"-"}^50}')
print(f'{"NOME":<10}{"AV1":<10}{"AV2":<10}{"MÉDIA":<10}{"SITUAÇÃO":<8}')
for aluno in alunos:
    for key, value in aluno.items():
        if key == 'Nome':
            print(f'{value:<10}', end='')
        elif key == 'Nota':
            for cont in range(0, 2):
                print(f'{value[cont]:<10.2f}', end='')
        elif key == 'Média':
            print(f'{value:<10.2f}', end='')
        elif key == 'Situação':
            print(f'{value:>8}')
print('-'*50)
