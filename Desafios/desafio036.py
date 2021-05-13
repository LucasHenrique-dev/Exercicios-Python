valor = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Em quantos anos você pretende pagar: '))
mensal = valor/(anos*12)
valido = mensal <= salario*0.3
if valido:
    if anos == 1:
        print('O empréstimo foi aceito e você terá parcelas de R${:.2f} mensais durante {} ano'.format(mensal, anos))
    else:
        print('O empréstimo foi aceito e você terá parcelas de R${:.2f} mensais durante {} anos'.format(mensal, anos))
else:
    print('O empréstimo não foi aceito pois a taxa mensal de R${:.2f}'
          ' excedeu 30%(R${:.2f}) do valor do seu salário(R${:.2f})'.format(mensal, salario*0.3, salario))
