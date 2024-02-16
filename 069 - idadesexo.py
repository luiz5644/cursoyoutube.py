maiores = 0
h = 0
m = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Qual é a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é o seu sexo? [M/F] ')).upper().strip()[0]

    if idade > 18:
        maiores+=1
    if sexo == 'M':
        h +=1
    if idade < 20 and sexo == 'F':
        m += 1

    print('-'*20)
    resposta = ' '
    while resposta not in "SN":
        resposta= str(input('Você quer continuar ? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
    print('-'*20)

print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {m} mulheres com menos de 20 anos')