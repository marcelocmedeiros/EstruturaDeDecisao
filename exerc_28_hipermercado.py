# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
 porém não há limites para a quantidade de carne por cliente.
 Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
 Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário
 e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
 tipo de pagamento, valor do desconto e valor a pagar.
'''
print('=' * 43)
print('{:=^40}'.format(" PROGRAMA PARA HIPERMERCADO TABAJARA "))
print('=' * 43, '\n')

# variável escolha o tipo carne
carne = int(input('1 - File Duplo\n'
                       '2 - Alcatra\n'
                       '3 - Picanha\n'
                       'Qual tipo de pagamento: '))
# variável kilos
kilos = float(input('Quantos kilos de carne você deseja: '))
# tipo de pagamento
resposta = int(input("A compra será realizada com cartao Tabajara? 1p/ SIM - 2p/ NAO: "))
# declaração de preços das carnes
valor_fd = 4.90
valor_fd_5 = 5.80
valor_al = 5.90
valor_al_5 = 6.80
valor_pi = 6.90
valor_pi_5 = 7.80

print('='*55)
# se File Duplo
if carne == 1:
    nome = "File Duplo"
    if carne <= 5:
        preco = kilos * valor_fd
    elif carne > 5:
        preco = kilos * valor_fd_5

# se Alcatra
elif carne == 2:
    nome = "Alcatra"
    if carne <= 5:
        preco = kilos * valor_al
    else:
        preco = kilos * valor_al_5
# se Picanha
elif carne == 3:
    nome = "Picanha"
    if carne <= 5:
        preco = kilos * valor_pi
    else:
        preco = kilos * valor_pi_5
# cartão Tabajara
if resposta == 1:
    r = "SIM"

    desconto = ((preco * 5) /100)
    total = preco - desconto
else:
    r = "NAO"
    total = preco
print("\n***************************CUPOM FISCAL**************************************")
print("* Carne.......................................................... %s " % nome)
print("* Quantidade..................................................... %d KG " % kilos)
print("* Preço......................................................... %2.f R$ " % preco)
print("* Cartao Tabajara................................................ %s " % r)
print("* Total com desconto............................................ %2.f R$ " % total)
print("******************************************************************************")