turma = []
aluno = []
while True:
    aluno.append(str(input('Informe o nome: ')).strip().title())
    for c in range(0, 2):
        nota = (float(input(f'Informe a {c+1}° nota: ')))
        while nota > 10 or nota < 0:
            nota = float(input('Valor inválido: '))
        aluno.append(nota)
    turma.append(aluno[:])
    aluno.clear()
    resp = str(input('Deseja continuar[S/N]: ')).strip().lower()[0]
    while resp not in 'sn':
        resp = str(input('Opção inválida, tente novamente[S/N]: ')).strip().lower()[0]
    if resp == 'n':
        break
print(f'{"N°":<5}{"Nome":<10}{"Média":>8}')
print('-'*25)
for pos, info in enumerate(turma):
    print(f'{pos:<4} {info[0]:<10} {(info[1]+info[2])/2:>6.2f}')
print('Se desejas saber os detalhes sobre o aluno, digite seu número')
while True:
    escolha = str(input('Deseja saber a nota de alguém[S/N]: ')).strip().lower()[0]
    while escolha not in 'sn':
        escolha = str(input('Opção inválida, por favor digite novamente[S/N]: ')).strip().lower()[0]
    if escolha == 'n':
        break
    numero = int(input('Qual o número: '))
    while numero > len(turma)-1 or numero < 0:
        numero = int(input('Número inválido, digite novamente: '))
    print(f'''As notas de {turma[numero][0]} são:
N1° -> {turma[numero][1]}
N2° -> {turma[numero][2]}''')
