# exemplo de codigo para tratamento de erros em python

try:
  num = int(input('Digite um numero inteiro: '))
  print(f'\nO número fornecido foi {num}')

except Exception as erro:
  print(f'O erro encontrado foi {erro.__class__}')
