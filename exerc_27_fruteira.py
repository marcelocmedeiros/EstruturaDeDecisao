# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
 Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
 receberá ainda um desconto de 10% sobre este total.
 Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
 adquiridas e escreva o valor a ser pago pelo cliente.
'''
print('=' * 43)
print('{:=^40}'.format(" PROGRAMA PARA BARRACA DE FRUTAS "))
print('=' * 43, '\n')

# variável kilos de morangos e maçãs
morangos = float(input('Quantos kilos de morangos você quer comprar: '))
macas = float(input('Quantos kilos de maçãs você quer comprar: '))
# declarando preço das variáveis
valor_mor = 2.50
desc_mor = 2.20
valor_mac = 1.80
desc_mac = 1.50
# declaranto totalidade de peso da compra
kilos = morangos + macas

# analisando quantidade e valor da compra dos morangos
if  morangos <= 5:
    valor_tot_mor = valor_mor * morangos

elif morangos > 5:
    valor_tot_mor = desc_mor * morangos

if  macas <= 5:
    valor_tot_mac = valor_mac * macas

elif macas > 5:
    valor_tot_mac = desc_mac * macas
# soma das compras
valor_final = valor_tot_mac + valor_tot_mor
# desconto extra caso compras < R$ 25 kilos > 8
if valor_tot_mac + valor_tot_mor >25 or kilos > 8:
    valor_final = (valor_tot_mac + valor_tot_mor) - ((valor_tot_mac + valor_tot_mor) * 0.1)

print('='*35)
print(f' Você comprou {morangos:.2f}kg de morangos\n '
      f'E comprou mais {macas:.2f}kg de maçãs.\n'
      f'Totalizando {kilos:.2f}Kg')
print('='*35)

print(f'O valor dos morango é R${valor_tot_mor:.2f}')
print(f'O valor da compra de maçãs é R${valor_tot_mac:.2f}')
print(f'O valor total de suas compra foi R${valor_final:.2f}')
print('='*35,'\n')




