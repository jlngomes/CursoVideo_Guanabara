
#--- Exercício 036 ---#

valor = float(input("\nQual o valor da casa: "))

salario = float(input("\nQual o salário: "))

anos = int(input("\nQuantos anos de financiamento: "))

#Rules
prestacao = valor / (anos * 12)
minimo = (salario * 30) / 100

#Visualizar
print(f'\nPara pagar uma casa de R${valor} em {anos} anos a prestação será de {prestacao}')

#Condição
if prestacao <= minimo:
    print("\nEmpréstimo aprovado!!")
else:
    print("\nEmpréstimo reprovado!!")
