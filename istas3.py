# pessoas = []
# dados = ['pedro', 25,'maria', 19,'joão', 15]


# pessoas.append(dados[:]) #eu to fazendo aqui uma cópia da lista 'dados', e colocando a lista dados dentro da lista 'pessoas'

# print(pessoas[1])

# pessoas = []
# pessoas.append('luiz')
# pessoas.append(20)
# galera = []

# galera.append(pessoas[:])

# pessoas[0] = 'ana'
# pessoas[1] = 40

# galera.append(pessoas[:])

# print(galera)

# galera = [['joão', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]

# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')


galera = []
dado = []
totmai = 0
totmen = 0
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} já é de maior :)')
        totmai +=1
    else:
        print(f'{p[0]} ainda é menor de idade :/')
        totmen += 1

print(f'temos {totmai} maiores e {totmen} menores de idade')