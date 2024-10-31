
#--- Exercício 004 ---#

text = input('\nDigite algo: ')

print(f'\nO tipo primitivo desse elemento é {type(text)}')
print(f'\nSó tem espaços, {text.isspace()}')
print(f'\nSó tem números, {text.isnumeric()}')
print(f'\nÉ alfabético, {text.isalpha()}')
print(f'\nÉ alfanumérico, {text.isalnum()}')
print(f'\nEstá em maiúscula, {text.isupper()}')
print(f'\nEstá em minúscula, {text.islower()}')
print(f'\nEstá capitalizado, {text.istitle()}')



