# @title Exemplo de estrutura de decisão aninhada cpm elif

print('Olá! Qual categoria do produto que você gostaria? \nEscolha entre 1, 2, 3, 4 ou 5')

cat = int(input("selecione a categoria desesajada para ver o preço: "))

if cat == 1:
    preco = 10,00
elif cat == 2:
    preco = 18,00  
elif cat == 3:
    preco = 23,00
elif cat == 4:
    preco = 26,00        
elif cat == 2:
    preco = 31,00
else:
    print('Número inválido. \nTente novamente')
    preco = 0

print(f'O preç]o do produto é: R${preco}')
