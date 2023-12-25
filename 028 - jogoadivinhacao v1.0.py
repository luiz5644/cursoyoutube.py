#o computador vai gerar um numero de 0 a 5, se a resposta do jogador for == a respota do computador, o usuário ganha, se não ele perde

from random import randint
from time import sleep

computador = randint(0,5)

print (22* '-*' )
print ('\033[1;34mestou pensando em um numero entre 0 e 5....\033[m')
print (22* '-*' )

sleep(2)

jogador = int(input('\033[1;34mvocê sabe qual é ?????\033[m'))


print('processando resposta......')
sleep(2)


if jogador == computador:
    print('\033[1;32m parabéns, você acertou\033[m')

else:
    print ('\033[1;31m iiii você errou, que pena..... tente novamente\033[m')
