
#--- Exercício 044 ---#

print('=' * 10, end=' ')
print('Loja do DEV Python', end=' ')
print('=' * 10)

preco = float(input('\nPreço das compras: R$ '))

print('\nFORMAS DE PAGAMENTO')

opcao = int(input('[1] á vista dinheiro/cheque\n'
              '[2] á vista cartão\n'
              '[3] 2x no cartão\n'
              '[4] 3x ou mais no cartão\n'
              '\nDigite sua opção: '))

if opcao == 1:
    valor_1 = preco - ((preco * 10)/100)
    print(f'\nÁ vista tem desconto de 10%, o valor da sua compra era de R${preco:.2f} e com o desconto '
                                                                                            f'foi para R${valor_1:.2f}')
elif opcao == 2:
    valor_2 = preco - ((preco * 5) / 100)
    print(f'\nÁ vista no cartao tem desconto de 5%, o valor da sua compra era de R${preco:.2f} e com o desconto '
                                                                                            f'foi para R${valor_2:.2f}')
elif opcao == 3:
    print(f'\n2x no cartão continua o mesmo preço, o valor a se pagar é de R${preco:.2f}')

elif opcao == 4:
    parcelas = int(input('Quantas vezes quer parcelas? '))
    valor_3 = (preco + ((preco * 20) / 100)) / parcelas
    print(f'\nSua compra será parcelada em {parcelas}x de R${valor_3:.2f} COM JUROS\n'
                                 f'Sua compra no valor de R${preco:.2f} vai custar no final R${valor_3 * parcelas:.2f}')

else:
    print('Opção inválida, tente novamente')
