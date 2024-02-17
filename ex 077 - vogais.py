palavras = 'aprender', 'progamar', 'limguagem', 'python', 'curso', 'gratis', 'estudar', 'preticar', 'trabalhar', 'mercado', 'programador', 'futuro'
# tumpla

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    
