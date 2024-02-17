# def mostralinha():
#     print(20*'-')


# mostralinha()

# def titulo(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)


# titulo(' kokooko')
# titulo('meu deus okoko deu certo')

# ////////////////////////////////////////////////////////////

# def soma(n1, n2):
#     s = n1 + n2
#     print(f'esse é o seu numero 1: {n1} e esse é o seu número 2: {n2}, a soma deles dois é {s}')


# n1 = int(input('numero 1: '))
# n2 = int(input('numero 2: '))

# soma(n1, n2)

# ////////////////////////////////////////////////////////////

# def contador(*num):
    # print (len(num))

    # for valor in num:
    #     print(f'{valor} ', end='')
    # print('fim')

    # tam = len(num)
    # {len(num)}
    # print(f'recebi os valores {num} e são ao todo {tam} números')


# contador(2, 3, 4, 8, 5)
# contador(8, 5)
# contador(5, 2, 8)

# ////////////////////////////////////////////////////////////

# def dobra(lst):
#     pos=0
#     while pos < len(lst):
#         lst[pos]*= 2
#         pos += 1


# valores=[1, 2, 5, 8, 8, 7]
# dobra(valores)
# print(valores)

# ////////////////////////////////////////////////////////////

def soma2(* valores):
    s = 0 
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')

soma2(5, 10)
soma2(2, 5, 2, 1, 5)