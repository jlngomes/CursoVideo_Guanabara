
#--- Exercício 052 ---#

n = int(input('Digite um número para leitura: '))
tot = 0

for i in range(1, n+1):
    if n % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{i}', end=' ')

print(f'\n\033[mO numéro {n} foi divisível {tot} vezes')
if tot == 2:
    print('Este número digitado é primo')
else:
    print('Este número digitado não é primo')
