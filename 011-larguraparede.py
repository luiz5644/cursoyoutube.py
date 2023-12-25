#largura e altura de uma parede em metros, area e quantidade de tinta nescessaria para pintar, sabendo qie cada litro de tinta pinta uma area de 2m**2
l = float(input('qual é a largura da sua parede?'))
a = float(input('qual é a altura da sua parede:'))

area = l*a
tinta = area/2

print ('a sua parede tem {:.1f}M de altura e {:.1f}M de largura, sua área é de {:.1f}M², para pintala voce vai precisar de {:.1f}L de tinta'.format(a, l, area, tinta))