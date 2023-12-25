d = int(input('digite a distância da viajem:'))
vc= d * 0.50
vl = d * 0.45

print('Você vai iniciar agora uma viagem de {}Km'.format(d))

if d <= 200:
    print ('o valor fica de {:.2f} R$'.format(vc))
else:
    print ('o valor fica de {:.2f} R$'.format(vl))
