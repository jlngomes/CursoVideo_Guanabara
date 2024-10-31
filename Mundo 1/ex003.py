
#--- Exercício 003 ---#

### int() ---> certificando o input do usuário

num1 = int(input('\nDigite o primeiro valor: '))
num2 = int(input('\nDigite o segundo valor: '))

soma = num1 + num2

print(f'\nA soma entre os valores {num1} e {num2} é igual a {soma}')

#--- Previnindo o input do usuário para que seja um valor numérico ---#

num1 = input('\nDigite o primeiro valor: ')
num2 = input('\nDigite o segundo valor: ')

if not num1.isdigit() or not num2.isdigit():
    print('\nO valor inserido não é um valor numérico, corrija para usar corretamente o progama!')
else:
    soma = int(num1) + int(num2)
    print(f'\nA soma entre os valores {num1} e {num2} é igual a {soma}')

