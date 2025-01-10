
#--- Exercício 042 ---#

seg1 = float(input('\nSeguimento 1: '))
seg2 = float(input('Seguimento 2: '))
seg3 = float(input('Seguimento 3: '))

if seg1 < (seg2 + seg3) and seg2 < (seg1 + seg3) and seg3 < (seg2 + seg1):
    print('\nOs segmentos acima PODEM FORMAR triângulo ',end='')
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO')
    elif seg1 == seg2 != seg3 or seg1 != seg2 == seg3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('\nOs segmentos acima NÃO PODEM FORMAR triângulo')


