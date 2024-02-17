# parametro opcional

def soma(a=0, b=0, c=0):
# def soma(a=0, b=0, c=0):
# antes sem o parametro opcional, se eu não tivesse um valor para 'c' a def ia da erro, mas agora eu coloquei que se ela não receber nenhum valor, o valor dela é zero. Se eu quiser, eu posso fazer isso com todos os parametros (a=0, b=0, c=0).
    """
    isso faz a soma de 3 valores:
    a: primeiro valor
    b: segundo valor
    c: terceiro valor
    isso é um docstrings
    """
    s = a + b + c
    print(f'A soma vale {s}')

soma(3, 2, 5)
soma(8, 4)
soma(8)


# help(soma)