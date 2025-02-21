
#--- Exercício 055 ---#

aux_menor = 10000
aux_maior = 0

for i in range(1,6):
    peso = float(input(f'Peso da {i}º pessoa: '))
    if peso > aux_maior:
        aux_maior = peso
    if peso < aux_menor:
        aux_menor = peso

print(aux_maior)
print(aux_menor)

#--- Alternativa 1 ---#

aux_menor = 0
aux_maior = 0

for i in range(1,6):
    peso = float(input(f'Peso da {i}º pessoa: '))
    if i ==1:
        aux_maior = peso
        aux_menor = peso
    else:
        if peso > aux_maior:
            aux_maior = peso
        if peso < aux_menor:
            aux_menor = peso

print(f"Maior peso {aux_maior}")
print(f"Maior peso {aux_menor}")