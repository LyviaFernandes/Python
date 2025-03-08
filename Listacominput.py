# Inserindo dados em uma lista com ajuda dos usuarios

nave = list() #lista principal
aliens = list() #Nossa lista auxiliar

for a in range(0,5):
    aliens.append(str(input('Nome do alien:'))) #inserindo o nome
    aliens.append(str(input('Idade do alien:'))) #inserindo a idade
    nave.append(aliens[:]) #populando a lista principal
    aliens.clear() # apagando a lista auxiliar
    print('alien a bordo!!')

print('A nossa nave tem os aliens: ', nave)
