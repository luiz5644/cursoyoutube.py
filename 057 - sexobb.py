sexo1 = 'M'
sexo2 = "F"
sexo = 1

while sexo != 0:
    sexo = str(input('qual o sexo do bb ?')).upper()
    if sexo == sexo1:
        print('próximo bb')
    elif sexo == sexo2:
        print ('proximo bb')
    else:
        print('eu quero um sexo de bb')