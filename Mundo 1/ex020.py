
#--- Exercício 020 ---#

from random import shuffle

a1 = str(input('\nNome do primeiro aluno: '))
a2 = str(input('\nNome do segundo aluno: '))
a3 = str(input('\nNome do terceiro aluno: '))
a4 = str(input('\nNome do quarto aluno: '))

lista = [a1, a2, a3, a4]

shuffle(lista)

print(f'\nA lista na nova ordem é {lista}')