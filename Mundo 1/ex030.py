
#--- Exercício 030 ---#

from colorama import Fore

num = int(input('\nDigite um valor: '))

if num % 2 == 0:
    print(Fore.LIGHTBLUE_EX + '\nEste número é par!' + Fore.RESET)
else:
    print(Fore.CYAN + '\nEste número é ímpar' + Fore.RESET)