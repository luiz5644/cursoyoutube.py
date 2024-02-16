r = 'S'
soma = 0
c = 0  
maior = 0
menor = 0 

while r in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    c += 1

    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    r = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]

media = soma / c
print(f'''
A soma dos valores é igual a: {soma}
Quantidade de números digitados: {c}
Média dos números digitados: {media:.2f}
O maior número digitado foi: {maior}
O menor número digitado foi: {menor}''')

# print('A soma dos valores é igual a: {} Quantidade de números digitados: {} Média dos números digitados: {:.2f} O maior número digitado foi: {} O menor número digitado foi: {}'.format(soma,c,media, maior, menor ))