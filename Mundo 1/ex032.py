
#--- Exercício 032 --#

from datetime import date

ano = int(input('\nQual ano quer analizar? Coloque 0 para analizar o ano atual: '))

if ano == 0:
    ano = date.today().year #Pega o ano atual do computador

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} é NÃO BISSEXTO')