
#--- Exercício 019 ---#

from random import choice

a1 = str(input('\nNome do primeiro aluno: '))
a2 = str(input('\nNome do segundo aluno: '))
a3 = str(input('\nNome do terceiro aluno: '))
a4 = str(input('\nNome do quarto aluno: '))

lista = [a1, a2, a3, a4]

escolhido = choice(lista)

print(f'\nO aluno escolhido foi {escolhido}')