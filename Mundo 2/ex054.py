
#--- Exercício 054 ---#

from datetime import date

ano_nascimento = []
hoje = date.today().year

for i in range(0,7):
    ano = int(input(f'Em que ano nasceu a {i+1}° pessoa: '))
    ano_nascimento.append(ano)

maiores = 0
menores = 0

for j in ano_nascimento:
    idade = hoje - j
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'\nAo todo tivemos {maiores} pessoas maiores de idade \nE também tivemos {menores} pessoas menores de idade')

#--- Alternativa 1 ---#

from datetime import date

hoje = date.today().year

maiores = 0
menores = 0

for i in range(0,7):
    ano = int(input(f'Em que ano nasceu a {i+1}° pessoa: '))
    idade = hoje - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'\nAo todo tivemos {maiores} pessoas maiores de idade \nE também tivemos {menores} pessoas menores de idade')

