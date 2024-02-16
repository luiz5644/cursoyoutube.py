# a forma com eu fiz
# n=  soma = c = 0

# while n != 999:
#     n = int(input('Digite um número [999 para parar]: '))
#     if n != 999:
#         soma += n
#         c += 1
#     else:
#         print(f'Ao todo foram digitados {c} números, a soma dos números digitados foi: {soma}')
# print('FIM!')

# como o Guanabara fez
n=  soma = c = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))

print(f'Ao todo foram digitados {c} números, a soma dos números digitados foi: {soma}')