# vou colocar um número e ele vai dividir esse número, mostrar cada dígito 

n = int(input('Digíte aqui um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print ('A unidade do número é {}'.format(u))
print ('A dezena do número  é {}'.format(d))
print ('A centena do número é {}'.format(c))
print ('A unidade de milhar é {}'.format(m))

