#transforma de m para km, hm, dam, dm, cm e mm

m = float(input('Digite aqui a quantidade de metros que voce quer transformar:'))

km = m/1000
hm = m/100
dam = m/10
dm= m*10
cm = m*100
mm = m*1000

print('A distancia de {} M corresponde a\n{} KM\n{} HM\n{} DAM\n{:.0f} DM\n{:.0f} CM\n{:.0f} MM'.format(m, km, hm, dam, dm, cm, mm))

