valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um número: ')))
    r =str(input('Você quer continuar [S/N] ? '))
    if r in 'nN':
        break

for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

    
print('-='*30)
print(f'A sua lista completa é {valores}')
print(f'A lista de números pares é {pares}')
print(f'A lista de numeros ímpares é {impares}')
print(valores)