parenteses = str(input('digite a sua expressão: '))
npe= parenteses.count('(')
npd= parenteses.count(')')

if npe == npd:
    print('A sua expreessão é válida')
else:
    print('A sua expressão não é válida')

print(npe, npd)
# ele não fez desse mesmo jeito, mas pelo oq eu entendi ele só quer que eu olhe se os numeros de parenteses estão iguais de um lado e do outro, então da certo do mesmo jeito