
#--- Exercício 007 ---#

nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")

if not nota1.isdigit() or not nota2.isdigit():
    print('\nO valor inserido não é um valor numérico, corrija para usar corretamente o progama!')
else:
    media = (float(nota1) + float(nota2)) / 2
    print(f'\nA soma entre os valores {nota1} e {nota2} é igual a {media}')

#--- Alternativa ---#

array_num = []
soma_total = 0
check = True
while check:
    nota = input('\ninsira sua nota: ')
    if not nota.isdigit():
        print('\nO valor inserido não é um valor numérico, corrija para usar corretamente o progama!')
        continue
    array_num.append(int(nota))

    resposta = input('\nGostaria de continuar <S/N>: ')

    if resposta.upper() == 'N':
        for num in array_num:
            soma_total += num
        media = soma_total / len(array_num)  # ---> outra opção: media = sum(array_num)/len(array_num)
        check = False

print(f'\nA média total de todos os valores inseridos é igual a {media}')
