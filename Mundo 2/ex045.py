
#--- Exercício 045 ---#

from random import choice

lista_opcao = ['PEDRA', 'PAPEL', 'TESOURA']

escolha_computador = choice(lista_opcao)

escolha_jogador = int(input('[1] PEDRA\n'
                            '[2] PAPEL\n'
                            '[3] TESOURA\n'
                            '\nQual a sua jogada? '))

print('\nJO'
      '\nKEN'
      '\nPO!!!\n')

print('-=' * 10)
print(f'Computador jogou {escolha_computador}')
print(f'O jogador jogou {lista_opcao[escolha_jogador - 1]}')
print('-=' * 10)

if escolha_jogador == 1 and escolha_computador == 'PAPEL':
    print('\nCOMPUTADOR VENCE')
elif escolha_jogador == 1 and escolha_computador == 'PEDRA':
    print('\nEMPATE')
elif escolha_jogador == 1 and escolha_computador == 'TESOURA':
    print('\nJOGADOR VENCE')

elif escolha_jogador == 2 and escolha_computador == 'PAPEL':
    print('\nEMPATE')
elif escolha_jogador == 2 and escolha_computador == 'PEDRA':
    print('\nJOGADOR VENCE')
elif escolha_jogador == 2 and escolha_computador == 'TESOURA':
    print('\nCOMPUTADOR VENCE')

elif escolha_jogador == 3 and escolha_computador == 'PAPEL':
    print('\nJOGADOR VENCE')
elif escolha_jogador == 3 and escolha_computador == 'PEDRA':
    print('\nCOMPUTADOR VENCE')
elif escolha_jogador == 3 and escolha_computador == 'TESOURA':
    print('\nEMPATE')

#--- Alternativa 1 ---#

from random import randint

lista_opcao = ['PEDRA', 'PAPEL', 'TESOURA']

escolha_computador = randint(0,2)

escolha_jogador = int(input('[1] PEDRA\n'
                            '[2] PAPEL\n'
                            '[3] TESOURA\n'
                            '\nQual a sua jogada? '))

print('\nJO'
      '\nKEN'
      '\nPO!!!\n')

print('-=' * 10)
print(f'Computador jogou {escolha_computador}')
print(f'O jogador jogou {lista_opcao[escolha_jogador - 1]}')
print('-=' * 10)

if escolha_computador == 0:
    if escolha_jogador == 0:
        print('\nEMPATE')
    elif escolha_jogador == 1:
        print('\nJOGADOR VENCE')
    else:
        print('\nCOMPUTADOR VENCE')

if escolha_computador == 1:
    if escolha_jogador == 0:
        print('\nCOMPUTADOR VENCE')
    elif escolha_jogador == 1:
        print('\nEMPATE')
    else:
        print('\nJOGADOR VENCE')

if escolha_computador == 2:
    if escolha_jogador == 0:
        print('\nJOGADOR VENCE')
    elif escolha_jogador == 1:
        print('\nCOMPUTADOR VENCE')
    else:
        print('\nEMPATE')
