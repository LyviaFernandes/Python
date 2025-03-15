
try:
  a = int(input('Entre com o numerador:'))
  b = int(input('Entre com o denominador:'))

  conta = a / b 

except ZeroDivisionError:
  print('NÃO DIVIDE POR ZERO')

except KeyboardInterrupt:
  print('O usuario quis sair')

except (ValueError, TypeError):
  print('Digite um numero inteiro!!!\n')
except Exception as errado:
  print(f'O erro encontrado foi {errado.__class__}')

else:
  print(f'o resultado de {a} e {b} é {conta:.3f}\n')

finally:
  print('A pratica leva a perfeição. \nContinue assim.')
