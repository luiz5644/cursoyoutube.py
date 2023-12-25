''''co = float(input('Qual o comprimento do cateto oposto:'))
ca = float(input('Qual o comprimento do cateto adjacente:'))

h = (co**2 + ca**2) ** (1/2)


print('A sua hipotenusa vai medir {:.2f}'.format(h))'''
import math

co = float(input('Qual o comprimento do cateto oposto:'))
ca = float(input('Qual o comprimento do cateto adjacente:'))

h = math.hypot(co, ca)

print('a hipotenusa vai medir {:.2f}'.format(h))
