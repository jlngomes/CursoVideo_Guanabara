
#--- Exercício 051 ---#

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10-1) * r

for i in range(p, d + r, r):
    print(i, end=' -> ')
print('Acabou')