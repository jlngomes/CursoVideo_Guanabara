
#--- Exercício 005 ---#

num = input('Insira um número: ')

### Verifica se o usuário digitou corretamente ###

if not num.isdigit():
    print('\nO valor inserido não é um valor numérico, corrija para usar corretamente o progama!')
else:
      num = int(num)
      print(f'\nAnalizando {num}...\n'
            f'\nSeu antecessor é {num - 1} e seu sucessor é {num + 1}')