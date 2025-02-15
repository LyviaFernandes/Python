minutos = int(input('Quantos minutos você usou neste mês?'))

if minutos <= 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
print(f'\nVocê vai pagar este mês R${minutos * preco:6.2f}')
