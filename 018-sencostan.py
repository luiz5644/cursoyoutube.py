import math
a = float(input('digite aqui o ângulo que você deseja:'))

seno = math.sin(math.radians(a))
print('O seno de {}° é de {:.2f}'.format(a, seno))

cosseno = math.cos(math.radians(a))
print('O cosseno de {}° é {:.2f}'.format(a, cosseno))

tangente = math.tan(math.radians(a))
print('A tangente de {}° é de {:.2f}'.format(a, tangente))