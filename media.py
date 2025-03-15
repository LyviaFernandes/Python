def somalista(L):
    total = 0
    for e in L:
        total+= e
    return total

#definição  que calcula a média dos elementos da lista
def media_da_lista(L):
    comprimento = len(L)
    media = somalista(L) / comprimento
    return print(f'A média dos elementos da lista {L} é {media}')

lista = [7,6,10,8]

media_da_lista(lista)
