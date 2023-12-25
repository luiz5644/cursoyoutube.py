nc = str(input('Digite aqui o seu nome completo:')).strip()

print('analizando seu nome.....')

print('seu nome em maiusculo fica: {}'.format(nc.upper()))

print('o seu nome em minúsculo fica: {}'.format(nc.lower()))

print('o seu nome ao todo tem: {} letras'.format(len(nc) - nc.count(' ')))

#print('seu primeiro nome tem {} letras'.format(nc.find(' ')))

separa = nc.split()
print('seu primeiro nome é "{}" e ele tem {} letras'.format(separa[0], len(separa[0])))






