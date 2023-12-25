#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar 

#calcule o valor da prestação mansal, sabendo q ele não pode exceder 30por cento do salario ou então sera megado 

vc = float(input('Qual o valor da casa:R$'))
sc = float(input('Qual é o seu salário:R$'))
a = int(input('Em quantos snos vc pretende pagar essa casa:'))

vm = vc / (a * 12)
porcem = sc + (sc*30/100)

if vm <= porcem:
    print ('O pagamento mensal desta casa fica no valor de {:.2f}R$, você foi aprovado no imprestimo'.format(vm))

else:
    print ('O pagamento mensal desta casa fica no valor de {:.2f}R$, imfelizmente a parcela ultrapassou o valor de 30% acima do seu salário'.format(vm))


