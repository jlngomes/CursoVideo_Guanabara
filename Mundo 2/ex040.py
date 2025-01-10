
#--- Exercício 040 ---#

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media :float = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua nota foi de {media}, você está REPROVADO')
elif media >= 5 and not media >= 6.9:
    print(f'Sua nota foi de {media}, você está RECUPERAÇÃO')
else:
    print(f'Sua nota foi de {media}, você está APROVADO')