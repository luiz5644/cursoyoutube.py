# este mostra o dobro do meu numero, a sua raiz quadrada e raiz cubica
n = int(input('digite aqui um numero: '))
dob = n * 2
r2 = float(n ** (1/2))
r3 = float(n ** (1/3))

print("o seu numero é {}, o seu dobro é {}, a sua raiz quadrada é {} e sua raiz cubica é {:.4}".format(n, dob, r2, r3))

