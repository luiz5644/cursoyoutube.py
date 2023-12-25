# ate 9: mirim, ate 14: infantil, ate 19: junior, ate 20: senior e acima master

from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento do atleta: '))

idade = atual - nascimento 

if idade <= 9:
    print('O atleta tem {} anos e é MIRIM'. format(idade))

elif idade <= 14:
    print('O atleta tem {} anos e é INFANTIL'.format(idade))

elif idade <= 19:
    print ('O seu atleta tem {} anos e é JUNIOR' .format(idade))

elif idade <=25:
    print('O seu atleta tem {} anos e é SÊNIOR' .format(idade))

else:
    print('O seu a tleta tem {} anos e é MASTER'.format(idade) )
    
