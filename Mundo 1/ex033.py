
#--- Exercício 033 --#

num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('\nDigite o segundo número: '))
num3 = int(input('\nDigite o terceiro número: '))

num_maior = num1
num_menor = num1

#Menor número
if num2<num1 and num2<num3:
    num_menor = num2
if num3<num1 and num3<num2:
    num_menor = num3

#Menor número
if num2>num1 and num2>num3:
    num_maior = num2
if num3>num1 and num3>num2:
    num_maior = num3

print(f'\nO menor número digitado foi {num_menor}')
print(f'\nO maior número digitado foi {num_maior}')