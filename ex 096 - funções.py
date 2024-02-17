def titulo():
    print(19*'-')
    print('CONTROLE DE TERRENO')
    print(19*'-')
    print()

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terro {largura} x {comprimento} é de {area}M².')


titulo()
largura= float(input('Qual a largura(M) do terreno ? '))
comprimento = float(input('Qual o comprimento(M) do tereno? '))
print()
area(largura, comprimento)

