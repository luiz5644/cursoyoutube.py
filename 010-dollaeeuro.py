r = float(input('quantos reais voce tem:R$'))
#valor de cada moeda
dv = 4.98
ev = 5.45

# conversão
d = r/dv
e = r/ ev

print('hoje com o dollar a {}, e o Euro a {}\nvocê consegui comprar a quantidade de {:.2f}Dollares ou {:.2f} euros'.format(dv, ev, d, e))
