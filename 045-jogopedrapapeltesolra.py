#jogo pedra papel ou tesolra, ele tem que me mandar uma destas escolhas ao mesmo tempo que eu (assim como no jogo) e ver que ganha 
# import random
# from time import sleep

# print('vamos jogar')
# print('preparado...')
# sleep(2)
# print('pronto ou não, lá vou eu')
# sleep(2)
# e = ['pedra', 'papel', 'tesolra']
# escolha = random.choice(e)

# print ('a minha escolha é **{}**'.format(escolha))

# r=str(input('qual foi a sua ??'))

# if r =='pedra' and escolha == 'papel':
#     print('ganhei')

# elif r =='papel' and escolha == 'pedra':
#     print('vc ganhou')

# elif r == 'papel' and escolha == 'tesolra':
#     print('ganhei')

# elif r == 'tesolra' and escolha == 'papel':
#     print('vc ganhou')
    
# elif r == 'tesolra' and escolha == 'pedra':
#     print('ganhei')
    
# elif r == 'pedra' and escolha == 'tesolra':
#     print('vc ganhou')

# from time import sleep 
# import random
# print('''Suas opções:
# [ 0 ] PREDRA
# [ 1 ] PAPEL 
# [ 2 ] TESOURA ''')

# opção= int(input('Qual é a sua opção ? '))

# e = ['pedra', 'papel', 'tesolra']
# escolha = random.choice(e)


# print('JO')
# sleep (1)
# print ('KEN')
# sleep (1)
# print('PO!!')
# print ('papapapa')

# if opção  == '0' and escolha == 'pedra':
#     print('empate')
# elif opção == '1' and escolha == 'pedra':
#     print('vc perdeu')
# elif opção == '2' and escolha == 'pedra':
#     print('vc perdeu')

# elif opção  == '0' and escolha == 'papel':
#     print('vc perdeu')
# elif opção == '1' and escolha == 'papel':
#     print('empate')
# elif opção == '2' and escolha == 'papel':
#     print('vc ganhou')

# elif opção  == '0' and escolha == 'tesoura':
#     print('vc ganhou ')
# elif opção == '1' and escolha == 'tesoura':
#     print('eu ganhei')
# elif opção == '2' and escolha == 'tesoura':
#     print('empatou')



from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')

computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PREDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA ''')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep (1)
print ('KEN')
sleep (1)
print('PO!!')

print('-='*11)
print('computador jogou {}'.format(itens[computador]))
print ('jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0: #jogou pedra

    if jogador == 0:
        print('empate')

    elif jogador == 1:
        print('jogador vence')
    
    elif jogador == 2:
        print('computador vence')

    else: 
        print('jogada invalida')

elif computador ==1:
    if jogador == 0:
        print('computador vence')

    elif jogador == 1:
        print('empate')
    
    elif jogador == 2:
        print('jogador vence')
        
    else: 
        print('jogada invalida')

elif computador ==2:

    if jogador == 0:
        print('o jogador vence')

    elif jogador == 1:
        print('computador vence')
    
    elif jogador == 2:
        print('empate')
        
    else: 
        print('jogada invalida')
        

