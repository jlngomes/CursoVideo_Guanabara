
#--- Exercício 037 ---#

num = int(input('\nDigite um número inteiro: '))

print('\n[1] - Converter para BINÁRIO'
      '\n[2] - Converter para OCTAL'
      '\n[3] - Converter para HEXADECIMAL')

opcao = int(input('\nDigite sua opção: '))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para HEXADECIMAL é igual {hex(num)[2:]}')
else:
    print(f'{num} convertido para OCTA é igual {oct(num)[2:]}')
