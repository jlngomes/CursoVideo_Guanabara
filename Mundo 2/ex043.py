
#--- Exercício 043 ---#

peso = float(input('\nQual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))

imc : float = peso/(altura * altura)

print(f'\nO IMC dessa pessoa é {imc:.2f}')

if imc < 18.5:
    print('\nAbaixo do peso normal')
elif imc < 25:
    print('\nPeso ideal, parábens')
elif imc < 30:
    print('\nSobrepeso,')
elif imc < 40:
    print('\nObeso')
else:
    print('\nObesidade Mórbida')
