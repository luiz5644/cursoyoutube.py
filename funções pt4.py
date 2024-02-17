# def teste():
#     x = 8
    # iso é uma variável local, só vale na função teste
    # print(f'Na função teste, n vale {n}')
    # print(f'Na função teste, x vale {x}')

# programa principal
# n = 2 
# variável global, ela vale m todo o programa
# print(f'No programa principla, n vale {n}')
# teste()
# print(f'No programa principal, x vale {x}')

# ////////////////////////////////////////////////////////////

# def funcao():
#     n1 = 4
#     print(f'N1 dentro vale {n1}')
# programa principal
# n1 = 2 
# funcao()
# print(f'N1 fora vale {n1}')

# por mais que eu tenha duas variaveis com ps mesmos nomes, uma é global e a outra é local, então é como se o programa tivesse duas variavei com o mesmo nome. Isso é escopo de variaveis

# ////////////////////////////////////////////////////////////

# se eu quiser que um variante fique global no meu programa, como eu faço isso ?

# def funcao():
#     global n1
#     # assim eu to dizendo que essa variante local que ela não é mais local, ela agora é global, então o valor que vai aparecer é 'N1 = 4', aqui e no programa local.
#     n1 = 4
#     print(f'N1 dentro vale {n1}')

# # programa principal
# n1 = 2 
# funcao()
# print(f'N1 fora vale {n1}')


# ////////////////////////////////////////////////////////////

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os reesultados foram {r1}, {r2} e {r3}')