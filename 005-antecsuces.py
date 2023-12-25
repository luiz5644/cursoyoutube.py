#programa que le um numero e mostra o seu sucessor e seu antecessor
#pode ser feito de duas formas, na primeira eu adiciono 2 variaveis a mais, a variavel 'antecessor' e a variavel 'sucessor'. a segunda é dessa forma. Algo importante** quando eu diminuo linhas de códigos, eu estou economizando memoria, já que a cada variavel que eu atribuo ela é armazenada no meu pc.Mas se fosse necessário utlizar o valor de uma variante, mais de uma vez, eu tenho que fazer da primeira forma, atribuindo valor a ela, assim eu posso utilizar quando eu quiser.

n = int(input('coloque aqui um numero:'))

print("o seu numero é {}, o seu antecessor é {} e seu sucessor é {}".format(n, (n-1), (n+1)))