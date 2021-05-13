n1 = float(input('Digite o valor do seu salário: '))
if 0 <= n1 <= 1250.00:
    salario = n1*1.15
    print('O seu salário sofreu um aumento de 15% e agora é R$ {:.2f}'.format(salario))
elif n1 > 1250.00:
    salario = n1*1.1
    print('O seu salário teve um aumento de 10% e ficou R$ {:.2f}'.format(salario))
else:
    print('Valor inválido para um salário')
