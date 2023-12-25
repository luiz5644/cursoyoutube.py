
soma = 0
cont = 1
for c in range (1, 7):
    num =int(input('digite o seo {} valor'.format (cont)))
    if num % 2 ==0:
        soma += num
        cont += 1
    else:
        pass
print('a sua soma de valores é {}'.format(soma))

# for c in range (1, 10):
#     oi = str(input('digita'))
#     if oi != 'oi':
#         print('isso não é um oi')
#     else:
#         print('isso é um oi')
