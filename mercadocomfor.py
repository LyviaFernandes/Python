total = 0
vfeijao = 5.5
varroz = 4
vmacarrao = 2

for l in range (3):
    produto = input('Digite o código do primeiro produto: ')
    if produto == 'feijao':
        total += vfeijao 
    elif produto == 'arroz':
       total += varroz
    elif produto == 'macarrao':
        total += vmacarrao

print(f'o valor da sua compra é {total}')
