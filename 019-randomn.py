'''from random import choice
n1 = str(input('digite um nome:'))
n2 = str(input('digite um nome:'))
n3 = str(input('digite um nome:'))
n4 = str(input('digite um nome:'))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print ('o escolhido é \033[0;30;47m{}!!\033[m'.format(escolhido))'''

'''import random

print ('digite cores para ser escolhida de forma aleatória:')
cor1 = str(input('cor 1:'))
cor2 = str(input('cor 2:'))
cor3 = str(input('cor 3:'))

lista = [cor1, cor2, cor3]
escolhido = random.choice(lista)

print ('A cor escolhida é: {}'.format(escolhido))'''


from random import choice

print ('Digite cores para serem escolhidas de forma aleatória:')

c1 = str(input('cor 1:'))
c2 = str(input('cor 2:'))
c3 = str(input('cor 3:'))

lista = [c1, c2, c3]

escolha = choice(lista)

print ('a cor escolhida é:{}'.format(escolha))