# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(8)

# for v in valores:
#     print(f'{v}....', end='')
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}')
# print('cheguei no valor da lista')


a = [2, 3, 4, 7]
b = a [:] # uma cópia de 'a' dentro de 'b'
b [2] = 8

print (f'lista a: {a}')
print (f'lista b: {b}')