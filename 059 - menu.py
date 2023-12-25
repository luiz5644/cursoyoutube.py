somar = 1
multiplicar = 2
maior =3
novos_numeros = 4
sair_do_programa = 5
menu = 1
soma =0
n = 0


while True:
    n1 = int(input('número 1: '))
    n2= int(input('número 2: '))
    menu = int(input('oq vc quer fazer com esses numeros\n[1] soma\n[2] multiplicação\n[3] maior\n[4] add n\n[5] sair do programa:\n'))
    if menu== 1:
        print('o resultado de {} + {} = {}'.format(n1, n2, n1+n2))
        soma+= n
        break
    elif menu == 2:
        print('o resultado da multiplicação de {} * {} = {}'.format(n1, n2, n1+n2))
        break
    elif menu == 3:
        print('entre os o {} e {} o mairo numero é {}'.format(n1, n2, max(n1, n2)))
        break
    elif menu == 4:
        n3= int(input('mais um numero'))
        soma=+n3
    elif menu == 5:
        break
    else:
        print('pode repetir novamente?')

    



