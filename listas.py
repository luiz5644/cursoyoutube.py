# diferente das 'tunplas', listas são mutaveis e eu uso [] não ()
lanche = ['um', 'dois', 'três', 'quatro']
lanche[0] = 'dois'
# lanche.append('arroz') #se eu quiser adicionar algum item na minha lista

lanche.insert(2, 'droga') #se eu quiser adicionar algum item em uma posição específica

# del lanche[1] #apagar um item da lista

# lanche.pop() #apaga o ultimo item da lista
# #remove um item em específico

# if 'droga' in lanche:
#     lanche.remove('dois')

print (lanche)
# print (len(lanche))
# agora o 'um' é 'dois'