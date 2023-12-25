# idade para o exercito
from datetime import date
atual = date.today().year
ano=int(input('digite aqui seu ano de nacimento:'))
idade = atual - ano

if idade == 18:
    print('vc ta com {} anos, ta na hr'.format(idade))

elif idade < 18:
    print ('você tem {} anos, ainda não chegou a sua hora, mas resta apenas {} anos para voce ir'.format(idade ,18-idade))

    print ('Seu alistamento será em {}'.format(atual + (18-idade)))

elif idade > 18:
    print('voce tem {} anos, já passou da hora, se pasaram {} anos para vc se alistar'.format(idade,idade - 18))

    print('Seu alistamento foi em {}'. format(atual - (idade - 18)))
    
