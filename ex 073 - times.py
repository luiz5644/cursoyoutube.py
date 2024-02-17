times = 'Vitória', 'Criciúma', 'Juventude', 'Vila Nova', 'Atlético', 'Novohorizontino', 'Mirassol', 'Sport Recife', 'CRB', 'Guarani', 'ceará', 'botafogo', 'Avaí', 'Ituano', 'Sampaio Corrêa', 'Ponte preta', 'Tombense', 'Chapecoense', 'Londrina', 'ABC'

print('-=' * 15)
print(f'lista de times:\n{times}')
# for t in times:
#     print(t)
print('-=' * 15)
print(f'Os 5 primeiros times do Brasileirão: {times [0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense") +1}ª posição')

