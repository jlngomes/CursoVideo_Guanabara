
#--- Exercício 034 --#

salario = float(input('\nQual o salário a ser análisado: '))

if salario <= 1250:
    print(f'\nO valor do salário foi de R${salario} para R${(salario * 0.15) + salario} com 15% de reajuste')
else:
    print(f'\nO valor do salário foi de R${salario} para R${(salario * 0.10) + salario} com 10% de reajuste')