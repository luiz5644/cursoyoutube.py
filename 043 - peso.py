peso = float(input('Qual é o seu peso ? (Kg) '))
altura = float(input('Qual pe a sua altura (M) ? '))
input

imc = peso / (altura ** 2)
print('o seu imc é de: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')

elif imc <=25:
    print('Você está com o peso ideal')

elif imc <= 30:
    print('Você está com sobrepeso')

elif imc <=40:
    print('Você está obeso')
else:
    print('Você está com obesidade mórbida')