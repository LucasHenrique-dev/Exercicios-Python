times = ('sport', 'santa cruz', 'bota fogo', 'cruzeiro', 'arsenal', 'nautico', 'chapecoense', 'flamengo')
print(f'''Os 5 primeiros colocados foram: {times[:5]}
Os 4 últimos: {times[-1:-5:-1]}- (Do último até o 4 último)
OUTRO JEITO: Os 4 últimos: {times[-4:]}- (Do 4 último ate o último)
Os times em ordem alfabática são: {sorted(times)}
E o time da Chapecoense ficou em {times.index('chapecoense')+1}° lugar''')
