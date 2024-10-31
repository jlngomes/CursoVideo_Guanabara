
#--- Exercício 011 ---#

larg = float(input("\nQual a largura da sua parede: "))

alt = float(input('\nQual a altura da parede: '))

print(f'\nSua parede tem a dimensão de {larg}x{alt} e tem um area equivalente de {larg * alt:.6}m²')
print(f'\nPara a pintar essa parede, você precisará de {(larg * alt)/2:.6}L')
