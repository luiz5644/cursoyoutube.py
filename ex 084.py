# nome = []
# peso = []
# c = 0

# for c in range(0, 3):
#     nome.append(str(input('nome: ')))
#     c =+ 1
#     peso.append(float(input('peso: ')))

# print(f'No total foi cadastradas {c} pessoas, ')
# print(f'{nome[0]}e seu peso {peso[0]}')

temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'o maior peso foi de {mai}Kg. peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f' [{p[0]}] ', end='')

print()      
print(f'o menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
