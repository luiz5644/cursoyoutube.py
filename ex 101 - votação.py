def voto():
    from datetime import date
    atual = date.today().year
    print('-=' * 20)
    ano = int(input('Em que ano você nasceu ? '))
    idade = (atual - ano)
    
    if idade < 16:
        print(f'Com {idade} anos: NÃO PODE VOTAR.')

    elif idade <= 16 or idade < 18 or idade > 65:
        print(f'com {idade} anos: VOTO OPCIONAL.')

    else: 
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    
    print('-=' * 20)

voto()
    