
#--- Exercício 017 ---#

from math import pow,sqrt

co = (float(input('\nInsira o valor do cateto oposto: ')))

ca = (float(input('\nInsira o valor do cateto adjacente: ')))

hip = sqrt(pow(co,2) + pow(ca,2))

print(f'\nA hipotenusa é equivalente a {hip}')

#--- Alternativa 1 ---#

co = (float(input('\nInsira o valor do cateto oposto: ')))

ca = (float(input('\nInsira o valor do cateto adjacente: ')))

hip = (co ** 2 + ca ** 2) ** (1/2)

print(f'\nA hipotenusa é equivalente a {hip}')

#--- Alternativa 2 ---#

from math import hypot

co = (float(input('\nInsira o valor do cateto oposto: ')))

ca = (float(input('\nInsira o valor do cateto adjacente: ')))

hip = hypot(co,ca)

print(f'\nA hipotenusa é equivalente a {hip}')
