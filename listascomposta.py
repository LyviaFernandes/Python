

alunos = [] #nossa lista vazia

print('A lista depois de criada', alunos)

alunos.append('Ana') # inserindo o elemento 

print('A lista depois da inserção do primeiro elemento', alunos)

# Inserindo um outro elemento na lista 

alunos.append(22)

print(alunos)

turma = [] # Outra lista vazia

turma.append(alunos[:]) # inserindo a lista em outra lista

print(turma)

print(turma[0][0])
print(turma[0][1])
