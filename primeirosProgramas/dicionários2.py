grade = dict()
aluno = list()
notas = list()
for c in range(0, 3):
    grade['Nome'] = str(input('Nome: '))
    for c2 in range(0, 2):
        notas.append(int(input('Nota: ')))
    grade['Notas'] = notas[:]
    aluno.append(grade.copy())
    notas.clear()
print(aluno)
print(grade)
print(grade['Notas'][0])
for pos, info in enumerate(grade):
    print(f'{pos}, {info}')
    for r in info:
        print(r)
