from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!!')

def somapar(lista):
    soma = 0
    for valor in lista: 
        if valor % 2 == 0:
            soma+= valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = []
sorteia(numeros)
# print(numeros)
somapar(numeros)



# def sortvalores():
    
#     print(f'Sorteando os {len(valores)} valores da lista: {valores}, temos {random.choice(valores)}')

#     for v in valores:
#         if v % 2 ==0:
#             valores.append(pares)
#             print(f'Somando os valores pares de {valores}, temos {somap}')

# sortvalores()