
#--- Exercício 028 ---#

from random import randint

num = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
chance = int(input('\nEm que núimero eu pensei: '))
if chance == num:
    print('\nParábens, eu pensei no mesmo número')
else:
    print(f'\nErrou, eu pensei no número {num}')

#--- Alternativa melhorada ---#

from colorama import Fore
from random import randint
from time import sleep

num = randint(0,5)
print(Fore.YELLOW + '-=-' * 20 + Fore.RESET)
print(Fore.BLUE + 'Vou pensar em um número entre 0 e 5. Tente adivinhar...' + Fore.RESET)
print(Fore.YELLOW + '-=-' * 20 + Fore.RESET)
chance = int(input('\nEm que núimero eu pensei: '))
print(Fore.CYAN + '\nPROCESSANDO...' + Fore.RESET)
sleep(2)
if chance == num:
    print(Fore.GREEN + '\nParábens, eu pensei no mesmo número' + Fore.RESET)
else:
    print(Fore.RED + f'\nErrou, eu pensei no número {num}' + Fore.RESET)