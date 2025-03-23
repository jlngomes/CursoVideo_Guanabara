
#--- Exercício 053 ---#

frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
     inverso += junto[letra]

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('É um palíndromo está frase')
else:
    print('Não é um palíndromo está frase')

#--- Alternativa 1; Sem o for usando fatiamento ---#

# frase = str(input('Digite um frase: ')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = junto[::-1]
#
# print(f'O inverso de {junto} é {inverso}')
#
# if inverso == junto:
#     print('É um palíndromo está frase')
# else:
#     print('Não é um palíndromo está frase')