
#--- Exercício 023 ---#

num = int(input('Informe um numero: '))
print(f'Analizando o numero {num}')

print(f'Unidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')
