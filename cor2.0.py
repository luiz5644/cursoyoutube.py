nome = 'luiz'
cores = {'limpa':'\033[m',
         'azul':'\033[34m','amarelo':'\033[33m','pretoebranco':'\033[7m'}

print('{}{}{}'.format(cores['pretoebranco'], nome, cores['limpa'] ))
