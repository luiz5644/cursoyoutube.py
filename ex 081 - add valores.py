numeros = []

while True:
 numeros.append(int(input('Digite um numero: ')))
 r = str(input('você quer continuar [S/N]?'))
 if r == 'n' or r == 'N':
  break

print('-='*30)
print(f'Você digitou {len(numeros)} elementos')
print(f'Os valores em ordem decrescente são {sorted(numeros, reverse=True)}')
if '5' in numeros:
 print('O valor 5 foi encontrado dentro da lista')
else:
 print('O valor 5 não foi encontrado na lista')
print(f'A sua lista é: {numeros}')