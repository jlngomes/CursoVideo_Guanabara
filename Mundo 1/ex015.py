
#--- Exercício 015 ---#

km = int(input('\nQuantos KM você rodou: '))
dias = int(input('\nPor quantos dias alogou o carro: '))

total = (dias * 60) + (km * 0.15)

print(f'\nO valor a ser pago é de R${total}')
