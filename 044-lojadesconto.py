#calcule o valor a ser pago por um produto considerando o seu preço norma e condiçoes de pagamento; avista dinheiro/cheque:10% de desconto; avista no cartão: 5% de deconto; em ate 2x no cartão: preço normal; 3x no cartão: preço com juros de 20%

print('{:=^40}'.format('LOJAS LUIZ'))

preço = float(input('Digite o valor da compra: R$'))

print('''formas de pagamento 
[ 1 ] á vista no dinheiro/cheque
[ 2 ] á vista cartão 
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')

opção = int(input('Digite aqui a sua forma de pagamento: '))



if opção == '1':
    total = preço - (preço *10/100)

elif opção == '2':
    total = preço - (preço * 5 /100 )
    
elif opção ==3:
    total = preço
    parcela = total / 2
    print ('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))

elif opção == 4:
    total = preço + (preço * 20/100)
    totalparcelas = int(input('Quanta parcelas ?'))
    parcela = total / totalparcelas
    print("Sua compra será percela em {}x de R${:.2f} COM JUROS".format(totalparcelas, parcela ))
else:
    total = 0
    print("Opçao invalida de pagamento. Tente novamente")
print ('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
