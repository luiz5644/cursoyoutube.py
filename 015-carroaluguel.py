km = float(input('Quantos Km foram percorridos durante os dias de uso:Km'))
d = int(input('Com quantos dias voce ficou com o carro:'))

md = 60
mkm = 0.15
m = (km*mkm)+(d*md)

print('você ficou com o carro por {} dias, percorreu {}Km, o valor a ser pago é de {:.2f}R$'.format(d, km, m))