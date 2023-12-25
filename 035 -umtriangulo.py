
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim, os segmentos acima formam um triângulo')

else:
    print('Não, os segmentos acima não formam um triângulo')
