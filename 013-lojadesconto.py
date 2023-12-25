# tenho uma lojo, pagamentos a vista recebe 10% de desconto, se colocar 'luiz20' isso da 20rs de desconto avista, se for parcelado recebe um acressimo de 10%

v = float(input('Qual o valor da compra: R$'))
aoup = str(input('o valor vai ser pago avista ou parcelado:'))

#desconto 
desconto  = 10
d2 = 20
#acressimo
acressimo = 10
#para calcular alista ou prazo
vavista = v - (v*desconto/100)
#avista com cupom
avistacupom1 = v -(v*d2/100)
#valor parcelado
vparcelado = v + (v*acressimo/100)

#conduções
if aoup == 'avista':
    print('o valor de {:.2f}, avista com {}% de desconto fica por {:.2f}R$'.format(v, desconto, vavista))
#caso a pessoa digite 'avista20' ela recebe 20% de desconto, compra avista.
elif aoup == 'avista20':
    print('o valor de {:.2f}, com cupom de {:.2f}% de desconto fica por {:.2f}R$'.format(v, d2, avistacupom1))

else:
    print('o valor de {:.2f}, parcelado com {}% de acressimo fica por {:.2f}RS '.format(v, acressimo, vparcelado))

