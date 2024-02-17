from time import sleep

def linhas(): 
    print( '-=' *20)

   

# def contador(i, f, p):
#     print(f'contagem de {i} até {f} de {p} em {p}')
#     for i in range (i, f, p):
#         print(i, end=' ')
# essa def está errada poi se eu colocar um iniíco maior que o fim, ele não conta

def contador(i, f, p):
    if p < 0:
        p *= -1
    
    if p == 0:
        p =1
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print (f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont +=p
        print('Fim!')
    else: 
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print ('Fim!!')
       
linhas()
contador(1, 10, 1)
linhas()
contador(10, 0, 2) 
linhas()
print('Agora é a sua vez')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linhas()
contador(inicio, fim, passo)
