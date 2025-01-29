
#--- Exercício 048 ---#

cont = 0
soma = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
        cont += 1

print(f'A soma de todos os {cont} valores solicitados é de {soma}')
