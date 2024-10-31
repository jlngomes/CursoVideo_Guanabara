
#--- Exercício 016 ---#

from math import trunc

num = float(input('\nDigite um numero: '))

print(f'\nO número {num} tem a parte inteira {trunc(num)}')

#--- Alternativa 1 ---#

num = float(input('\nDigite um numero: '))

print(f'\nO número {num} tem a parte inteira {int(num)}')


