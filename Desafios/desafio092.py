from datetime import date
ano = date.today().year
dados = dict()
dados['Nome'] = str(input('Informe o nome: ')).strip().title()
nascimento = int(input('Informe o ano de nascimento: '))
while nascimento <= 0 or nascimento > ano:
    nascimento = int(input('Valor inválido, tente novamente: '))
dados['Idade'] = ano - nascimento
dados['CTPS'] = int(input('Informe a carteira de trabalho (0 caso não tenha): '))
if dados['CTPS'] > 0:
    dados['Contratação'] = int(input('Informe o ano de contratação: '))
    while dados['Contratação'] < nascimento or dados['Contratação'] > ano:
        dados['Contratação'] = int(input('Valor inválido, tente novamente: '))
    dados['Aposentadoria'] = (dados['Contratação'] - nascimento) + 35
    dados['Salário'] = float(input('Informe o salário: R$'))
    while dados['Salário'] < 0:
        dados['Salário'] = float(input('Valor inválido, tente novamente: '))
for key, value in dados.items():
    print('{}: {}'.format(key, 'Aposenta com {} anos'.format(value) if key == 'Aposentadoria' else value))
