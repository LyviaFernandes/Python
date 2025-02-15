#Exemplo de estrutura de decisão aninhada

print('Olá! Qual categoria do produto que você gostaria? \nEscolha entre 1, 2, 3, 4 ou 5')
cat1 = 10
cat2 = 18
cat3 = 23
cat4 = 26
cat5 = 31
cat = int(input("selecione a categoria desesajada para ver o preço: "))

if cat == 1:
    print(f'este produto custa R${cat1}')
else:
    if cat == 2:
        print(f'este produto custa R${cat2}')
    else:
        if cat == 3:
            print(f'este produto custa R${cat3}')
        else:
            if cat == 4:
                print(f'este produto custa R${cat4}')
            else:
                if cat == 2:
                    print(f'este produto custa R${cat2}')
                else:
                    print('Número inválido. \nTente novamente')
