
#--- Exercício 026 ---#

frase = str(input("Digite uma frase: ")).upper().strip()

cont_A = frase.count('A')
first_A = frase.find('A') + 1
last_A = frase.rfind('A') + 1

print(f'A letra A aparece {cont_A} vezes na frase')
print(f'A primeira letra A apareceu na prosição {first_A}')
print(f'A ultíma letra A apareceu na posição {last_A}')

