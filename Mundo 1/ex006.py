
#--- Exercício 006 ---#

num = input('Digite um valor: ')

if not num.isdigit():
    print('\nO valor inserido não é um valor numérico, corrija para usar corretamente o progama!')
else:
    num = int(num)
    print(f'\nO dobro de {num} é igual a {num * 2}'
          f'\nO triplo de {num} é igual a {num * 3}'
          f'\nRaiz quadrada de {num} é igual {num**(1/2)}')

#--- Alternativa ---#

import math

num = input('Digite um valor: ')

if not num.isdigit():
    print('\nO valor inserido não é um valor numérico, corrija para usar corretamente o progama!')
else:
    num = int(num)
    print(f'\nO dobro de {num} é igual a {num * 2}'
          f'\nO triplo de {num} é igual a {num * 3}'
          f'\nRaiz quadrada de {num} é igual {math.sqrt(num)}')