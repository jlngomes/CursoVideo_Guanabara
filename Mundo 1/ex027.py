
#--- Exercício 027 ---#

n = str(input("Digite seu nome completo: ")).strip()
nome = n.split()

first = nome[0]
last = nome[len(nome) - 1]

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {first}')
print(f'Seu último nome é {last}')