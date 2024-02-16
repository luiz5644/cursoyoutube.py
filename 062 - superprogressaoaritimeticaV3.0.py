print('Gerador de PA')
print('=-' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = p
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} -> ', end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Qauntos termos você quer mostrar a mais ? '))
print(f'Progressão finalizada com {total} termos mostrados')