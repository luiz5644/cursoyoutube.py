print('Gerador de PA')
print('=-' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p
c = 1
while c <= 10:
    print(f'{termo} -> ', end='')
    termo += r
    c += 1
print('Fim')