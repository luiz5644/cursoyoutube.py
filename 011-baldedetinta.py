# lata de tinta tem 18l, cada lata de tinta pinta 3M², cada balde de tinta custa 80R$, esse programa vai me mostrar quanto de tinta eu vou usar, valor a pagar e a quantidade de balde de tinta que eu vou usar 
area = float(input('Digite aqui a sua áres:'))
l = area/3
vl = (80/18)*l
lt = vl / 18
print('A área da sua parede é de {:.1f}M², a quantidade de litros de tinta nescessária é de {:.2f}L, o valor a ser pago é de {:.2f}R$, serão nescéssarios {:.0f} baldes de tinta'.format(area, l, vl, lt))