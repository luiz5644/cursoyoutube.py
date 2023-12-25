n =str(input('Digite seu nome completo: ')).strip()
nome =n.split()

print ('Muito prazer em te conhecer {}!!'.format(n[0]))

print('o seu primeiro nome é {}'.format(n[0]))

print ('Seu último nome é {}'.format(nome[len(nome)-1]))
