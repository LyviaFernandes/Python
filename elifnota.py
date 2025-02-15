# @title Exemplo de estrutura de decisão aninhada cpm elif

print('Olá Humano')

nota = float(input('Digite sua nota: '))

if nota <= 5:
    print(f'com a nota {nota}, você foi reprovado!')
    print('relaxa')
elif nota < 7:
    print(f'Com a nota {nota}, você está de recuperação')
else:
    print(f'Com a nota {nota} você foi aprovado! \nParabens!!!')

    print('\nFim do programa')
