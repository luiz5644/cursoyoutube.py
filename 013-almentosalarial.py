nome = str(input('Qual funcionario vai receber almento de salário?'))

salario= float(input('Qual o salário do seu funcionário: R$'))

aumento = 100

valor = salario + (salario*aumento/100)

print ('o funcionário {}, com {}% de aumento, passa a receber {:.2f}R$ de salário.'.format(nome, aumento, valor))
