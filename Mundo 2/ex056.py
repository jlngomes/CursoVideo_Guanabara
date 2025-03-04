
#--- Exercício 056 ---#

somaIdade = 0
mIdade = 0
maioridadeHomem = 0
nomeVelho = 0
totmulheres = 0

for p in range(1, 5):
    print(f"------ {p}º Pessoa ------")
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaIdade += idade
    if p == 1 and sexo in 'M':
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'M' and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'F' and idade < 20:
        totmulheres += 1

mIdade = somaIdade / 4
print(f'\nA média de idade do grupo é de {mIdade} anos')
print(f'O homem mais velho tem {maioridadeHomem} anos e se chama {nomeVelho}')
print(f'Ao todo são {totmulheres} mulheres com menos de 20 anos')
