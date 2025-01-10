
#--- Exercício 041 ---#

from datetime import date

nasc = int(input('\nDigite o ano do seu nascimento: '))

ano_atual = date.today().year

idade = ano_atual - nasc

if idade <= 9:
    print('\nClassificação: MIRIM')
elif idade <= 14:
    print('\nClassificação: INFANTIL')
elif idade <= 19:
    print('\nClassificação: JÚNIOR')
elif idade <= 25:
    print('\nClassificação: SÊNIOR')
else:
    print('\nClassificação: MASTER')

