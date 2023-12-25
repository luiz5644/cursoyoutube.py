nome = str(input('digite um nome:'))

if nome == 'luiz':
    print('o seu nome vai ficar assim:\033[4;30;46m{}\033[m'.format(nome))

elif nome == 'ana':
    print ('o seu nome vai ficar assim:\033[1;36;45m{}\033[m'.format(nome))

elif nome == 'caio': 
    print('o seu nome vai ficar assim:\033[7;31;40m{}\033[m'.format(nome))

else: 
    print('você não é especial, por isso seu nome vai ficar assim:{}'.format(nome))

