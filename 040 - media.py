n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))

m = (n1 + n2)/2

if m>= 7:
    print('COM A MÉDIA {:.1f} O ALUNO ESTÁ \033[4;32mAPROVADO\033[m'.format(m))

elif m >= 5 and m <= 6.9:
    print('COM A MÉDIA {:.1f}, O ALUNO ESTÁ DE \033[4;33mRECUPERAÇÃO\033[m'.format(m))

elif m < 5:
    print('COM A MÉDIA {:.1f}, O ALUNO ESTÁ \033[4;31mREPROVADO\033[m'.format(m))

