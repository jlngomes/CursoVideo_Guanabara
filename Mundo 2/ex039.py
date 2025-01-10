
#--- Exercício 039 ---#
from datetime import date

ano = int(input('\nQual ano você nasceu? '))
ano_atual = date.today().year

idade = ano_atual - ano

if idade < 18:
    print(f'\nAinda falta {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será no ano {idade + ano_atual}')
elif idade == 18:
    print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')
    print('Você TEM QUE SE ALISTAR IMEDIATAMENTE')
else:
    print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')
    print(f'Já devia ter se alistado há {idade - 18} anos')
    print(f'Seu alistamento foi em {ano_atual -(idade - 18)}')
