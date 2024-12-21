
#--- Exercício 022 ---#

nome = input("Digite seu nome completo: ")

print('Analizando seu nome...')

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúscula é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome é {nome.split(" ")[0]} e ele tem {len(nome.split(" ")[0])} letras')
