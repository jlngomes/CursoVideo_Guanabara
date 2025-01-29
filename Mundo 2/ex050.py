
#--- Exercício 050 ---#

soma_par = 0
for i in range(0,6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma_par += n

print(f'A soma dos valores pares digitados é de {soma_par}')