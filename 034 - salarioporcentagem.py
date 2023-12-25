salario = float(input('Digite aqui o seu salário atual:R$'))

aumento10= salario + (salario * 10/100)
aumento15 = salario + (salario * 15/100)


if salario <= 1250:
    print('O seu salário de {:.2f}R$, recebe um aumento de 15%, assim ele fica {:.2f}R$'.format(salario, aumento15))

else:
    print('O seu salário de {:.2f}R$, com um aumento de 10% fica {:.2f}R$'.format(salario, aumento10))

