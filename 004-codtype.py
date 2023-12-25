# o 'a' é um objeto, oque esta depois do a'.isalgo' é um método, então eu do valor a variante 'a' e o método me mostra o se ele é daquele tipo ou não 

a = input('Digite algo aqui:')

print('o tipo primitivo que vc digitou é:',type(a))
print('só tem espeços??', a.isspace())
print('é um numero??', a.isnumeric())
print('é alfabetico??',a.isalpha())
print('é alfanumerico??',a.isalnum())
print('está em maiusculas??',a.isupper())
print('esta em minusculas',a.islower())
print('esta captalizada',a.istitle())