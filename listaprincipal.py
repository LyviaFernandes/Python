nave = list() #lista principal
aliens = list() #Nossa lista auxiliar
escola = 0
trabalho = 0

for a in range(0,5):
    aliens.append(str(input('Nome do alien:'))) #inserindo o nome
    aliens.append(int(input('Idade do alien:'))) #inserindo a idade
    nave.append(aliens[:]) #populando a lista principal
    aliens.clear() # apagando a lista auxiliar
    print('alien a bordo!!')

    idade = nave[0][1]
    nave.clear()
    if idade < 18 :
        escola += 1
        print('este alien é um baby ainda')
    elif idade >= 18:
        trabalho += 1
        print('Esse alien é um jovem senhor')
print(f'temos {escola} babys e {trabalho} jovens senhores')
#print('A nossa nave tem os aliens: ', nave)
