# Colocando um titulo
print('\033[1;34m=\033[m' * 10, '\033[1;34mMaquina de Pagamento\033[m', '\033[1;34m=\033[m' * 10)
valor = float(input('Digite o valor do produto:'))
# 1 e 2 tem desconto de 10%
# 3 tem desconto de 5%
# 4 e 5 valor normal
# 6 ou mais valor com juros de 20%
print('''Qual será a forma de pagamento:
\033[37m[ 1 ] \033[4mÀ vista no dinheiro.\033[m
\033[37m[ 2 ] \033[4mÀ vista no pix.\033[m
\033[37m[ 3 ] \033[4mÀ vista no cartão.\033[m
\033[37m[ 4 ] \033[4mNo cartão em 2x sem juros.\033[m
\033[37m[ 5 ] \033[4mNo cartão em 3x sem juros.\033[m
\033[37m[ 6 ] \033[4mNo cartão em 4x ou mais com juros.\033[m''')

escolha = int(input('DIGITE A FORMA DE PAGAMENTO:'))

if escolha == 1 or escolha == 2:
    dinheiro_pix = valor - (valor / 100) * 10
    print('Sua compra será à vista.')
    print('O valor a pagar é de R${:.2f}, tendo um desconto de 10%.'.format(dinheiro_pix))
elif escolha == 3:
    cartao = valor - (valor / 100) * 5
    print('Sua compra será à vista no cartão.')
    print('O valor a pagar é de R${:.2f}, tendo um desconto de 5%.'.format(cartao))
elif escolha == 4:
    duas = (valor / 2)
    print('Sua compra será em 2x sem juros.')
    print('O valor a pagar é de R${:.2f}'.format(duas))
elif escolha == 5:
    tres = (valor / 3)
    print('Sua compra será em 3x sem juros.')
    print('O valor a pagar é de R${:.2f}'.format(tres))

elif escolha == 6:
    parcela = int(input('EM QUANTAS PARCELAS:'))
    if parcela < 4:
        print('\033[1;31mERRO no valor mínimo de parcelas.\033[m')
    else:
        # (J = P*i*t). formula para calcular o juros!
        quatro = valor + (valor * 0.02 * parcela)
        juros = quatro / parcela
        print('Sua compra será em {}x de R${:.2f} Com juros.'.format(parcela, juros))
        print('O valor final a pagar é de R${:.2f}.'.format(quatro))
else:
    print('\033[1;31mERRO na opção de pagamento. Tente novamente.\033[m')





