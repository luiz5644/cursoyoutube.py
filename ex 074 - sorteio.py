from random import randint
numeros= (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# print(f'Eu sorteei os valores {n}')

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print()
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')