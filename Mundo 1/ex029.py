
#--- Exercício 029 ---#

from colorama import Fore

lim_max: int = 80
km : int = int(input('\nQual a velocidade do carro: '))

if km <= lim_max:
    print(Fore.GREEN + '\nBoa viagem, dirija com cuidado!' + Fore.RESET)
else:
    valor_multa = float((km - lim_max) * 7)
    print(Fore.RED + '\nMULTADO, você excedeu o limite permitido que é de 80 km/h' + Fore.RESET)
    print(Fore.YELLOW + f'\nVocê deverá pagar uma multa de R${valor_multa}' + Fore.RESET)


