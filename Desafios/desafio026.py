n1 = str(input('Digite um nome: ')).strip().lower()
print(f'A letra "a" aparece {n1.count("a")}')
print(f'A primeira vez que a letra "a" aparece na frase é na posição: {n1.find("a")+1}')
print(f'A última vez que a letra "a" aparece no texto é na posição: {n1.rfind("a")+1}')
