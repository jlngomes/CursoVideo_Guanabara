
#--- Exercício 035 --#

print('-=' * 20)
print('Analisador de Triângulo')
print('-=' * 20)

seg1 = float(input('Seguimento 1: '))
seg2 = float(input('Seguimento 2: '))
seg3 = float(input('Seguimento 3: '))
if seg1 < (seg2 + seg3) and seg2 < (seg1 + seg3) and seg3 < (seg2 + seg1):
    print('\nOs segmentos acima PODEM FORMAR triângulo')
else:
    print('\nOs segmentos acima NÃO PODEM FORMAR triângulo')