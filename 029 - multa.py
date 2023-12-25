# se ele estiver a uma velocidade acima de 80km, ele recebe 7RS por KM ultrapassado
vl = float(input('a qual velocidade o veiculo estava?:'))

multa = (vl-80) * 7

if vl > 80:
    print('\033[;31mok voce estava a {:.2f} KM/hr e levou uma multa no valor de {:.2f}R$\033[m'.format(vl, multa))
else:
    print('não estava acima do limite de velocidade')

print('\033[;32mtenha um bom dia\033[m')    