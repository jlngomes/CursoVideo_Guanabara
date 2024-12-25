
#--- Exercício 031 --#

from colorama import Fore

distancia = int(input('\nDigite a distância da viagem: '))

if distancia <= 200:
    passagem_curta = distancia * 0.450
    print(Fore.GREEN + f'\nO valor da passagem ficou em R${float(passagem_curta)}' + Fore.RESET)
else:
    passagem_longa = distancia * 0.45
    print(Fore.GREEN + f'\nO valor da passagem ficou em R${float(passagem_longa)}' + Fore.RESET)