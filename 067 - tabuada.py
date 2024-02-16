n = 0
c = 0
while True:

    n = int(input('Quer ver a tabuada de quel valor? '))
    if n > 0:

        print('-'*15)
        for c in range(1, 11):
            print(f''' {n} X {c} = {c*n}''')
        print('-'*20)
    else:
        print('PROGRAMA TABUEADA ENCERRADO. Volte sempre!')
        break