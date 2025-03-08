filme = {'Titulo': 'Star Wars','Diretor':'George Lucas', 'ano': 1977}

print(filme)

print(filme.keys())
print(filme.values())

for k in filme.keys():
    print(k)
for v in filme.values():
    print(v)
print()
for k,v in filme.items():
    print(f'{k} é {v}')
