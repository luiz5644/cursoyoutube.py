#ele vai me pedir dois numeros inteiros e eu vou dizer qual dos dois é o maior

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))

if n1 > n2:
    print ('O primeiro número é maior {}'.format(n1))
    
elif n2 > n1:
    print('O segundo número é maior {}'.format(n2))

else:
    print('Os dois valores são iguais')
