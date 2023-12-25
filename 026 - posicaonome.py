nome = str(input('Digite aqui algo aqui: ')).lower().strip()

print ('A letra "A" a aparece {} vezes'.format(nome.count('a')))

print ('A primeira letra "A" apareceu na posição {}'.format(nome.find("a")+1))

print  ('A última letra "a" apareceu na posição {}'.format(nome.rfind('a')+1))