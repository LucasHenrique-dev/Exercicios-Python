filme = {'Filme': 'Star Wars', 'Ano': '1987', 'Diretor': 'George Lucas'}
print(filme)
print('-='*30)
for pos, info in filme.items():
    print(f'{pos} e {info}')
print('-='*30)
for pos, info in enumerate(filme):
    print(f'{pos}, {info}')
print('-='*30)
print(filme.keys())
print(filme.values())
print(filme.items())
print(f'O filme {filme["Filme"]} foi criado em {filme["Ano"]} pelo diretor {filme["Diretor"]}')
filme['Avaliação'] = 'Ótimo filme'
filme['Ano'] = 1986
print('-='*30)
print(filme.items())
print('-='*30)
del filme['Avaliação']
print(filme.items())
