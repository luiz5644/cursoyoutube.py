cont = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco'

while True:
    num = int(input('digite um número entre 0 e 5: '))
    if 0<= num <= 5:
        break
    print ('tente novamente', end='')
    
print(f'Você digitou o número {cont[num]}')