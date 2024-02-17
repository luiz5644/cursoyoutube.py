numeros = []
maior = 0
menor = 0

for c in range(1, 6):
    numeros.append(int(input(f'digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = numeros[c]
        
    else:
        if numeros[c] > maior:
            maior = numeros[c]
            
        elif numeros[c] < menor:
            menor = numeros[c]

print('=-' * 30)
print(f'você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}... ', end='')
print()