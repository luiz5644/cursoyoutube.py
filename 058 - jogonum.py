from random import randint
from time import sleep
computador = randint(2, 3)
r = 1
c = 0

while r != 0:
    print("\033[7;33;40m eu estou pensando em um número, sabe qual é ?\033[m")
    r = int(input('digite um número'))
    c += 1 
    if r == computador:
        sleep(2)
        print('\033[1;32;45mparabens, vc acertou e ganhou o jogo. o seu numero de tentativa foi de {}\033[m'.format(c))
        break

        
        
    else:
        sleep(2)
        print(" que pena, tente novamente")
        
        