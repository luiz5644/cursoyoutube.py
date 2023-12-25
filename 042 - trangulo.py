s1 = int(input('primeiro segmento: '))
s2 = int(input('segundo segmento: '))
s3 = int(input('terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triângulo!')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Os segmentos acima não podem formar um triângulo')