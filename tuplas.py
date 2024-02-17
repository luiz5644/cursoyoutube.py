# uma variável que pode guardar vários valóres = tupla
# e tuplas são imutávei

# lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
# print (lanche[1:3])

# lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
# lanche [1]= 'Refrigerante'
# print (lanche[1]) 
# da erro, pois eu estou tentando alterar o valor 1 da minha tupla, de um 'Suco' para um 'Refrigerante'

# lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
# print (lanche[-1])

# formatando uma tumbla
#sem posição 
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# for comida in lanche:
#     print(f'eu vou querer 1 porção de {comida}')

# com posição 

# for cont in range(0, len(lanche)):
#     print(f'eu vou comer {lanch[cont]} na posição {cont}')

# com posição 

# for pos, comida in enumerate(lanche):
#     print(f'eu vou comer {comida} na posição {pos}')
# print('tudo lá pra casa')

#colocando em ordem 
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# print(sorted(lanche))


# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a
# print (len(c)) quantas coisas tem no c = 7
# print (c.count(5)) quantos 5 aparecem = 2
# print (c.index(4)) posição do item 4 = 6


# pessoa = ('gustavo', 39, 'm', 99.88)
# del (pessoa) uma forma de apagar uma tupla, eu não posso apagra um item em específico, mas eu posso apagra uma tupla inteira
# print(pessoa)