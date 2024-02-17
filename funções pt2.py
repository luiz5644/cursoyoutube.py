def contador(i, f, p):

    """
    faz uma contagem e mostra na tela.
    param i: início da contagem
    param f: fim da contagem 
    param p: passo da contagem 
    :return: sem return
    função criada por luiz
    """
    # isso acima uma docstrings, é tipo um comentário que eu crio que serve para explicar uma parte do meu cod. quando eu vou e escrevo help(contador) essa instruções aparecem

    c = i
    while c <= f:
        print(f'{c}', end='..')
        c+=p
    print('fim')

contador()

# help(contador)