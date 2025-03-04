
#--- Exercício 057 ---#

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos, Informe seu sexo novamente: [M/F] ')).strip().upper()[0]

if sexo == 'M':
    print(f"Sexo Masculino registado com sucesso")
else:
    print(f"Sexo Feminino registado com sucesso")