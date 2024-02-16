total = 0
maisde1000 = 0
menorpreço = 0
c = 0 
barato = ''
while True:
    nomeproduto = str(input('nome do produto: '))

    preço = float(input('Preço: R$ '))
    c += 1
    total+= preço

    if preço > 1000:
        maisde1000 += 1

    if c == 1 or preço < menorpreço:
        menorpreço = preço
        barato = nomeproduto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if resposta == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisde1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menorpreço:.2f}')