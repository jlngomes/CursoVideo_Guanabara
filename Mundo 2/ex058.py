
#--- Exercício 058 ---#

from random import randint

num = randint(0,10)
print('-=-' * 30)
print('Olá, sou o seu computador e vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 30)

jogadas = True
tentativas = 1

while jogadas:
    chance = int(input('Qual o seu palpite: '))
    if chance == num:
        jogadas = False
    elif chance < num:
        print('mais...Tente outra vez')
        tentativas += 1
    else:
        print('Menos...Tente outra vez')
        tentativas += 1

print(f'Acertou com {tentativas} tentaivas, Parabéns!')

