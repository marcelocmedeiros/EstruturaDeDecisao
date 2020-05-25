# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90..
'''
print('=' * 43)
print('{:=^40}'.format(" PROGRAMA PARA O POSTO DE COMBUSTÍVEL "))
print('=' * 43, '\n')

# variável A-álcool, G-gasolina
combustivel = str(input('Qual o tipo de combustível digite\n'
                        'A-álcool\n'
                        'G-gasolina: ')).strip().upper()

# valor do abastecimento
alcool = 1.90
gasolina = 2.50
# condição para os descontos de alcool e gasolina
if combustivel == "A":
    # quantidade de litro
    litros = float(input('Quantos litro deseja abastecer: '))
    valor_alc = litros * alcool
    if litros <= 20:
        desco = valor_alc - (valor_alc * 0.03)
    else:
        desco = valor_alc - (valor_alc * 0.05)
    print(f'Você abasteceu com Alcool e colocou {litros:.2f}l\n'
          f'O valor sem desconto é R${valor_alc:.2f}\n'
          f'Mas na promoção você vai pagar R${desco:.2f}')
elif combustivel == "G":
    # quantidade de litro
    litros = float(input('Quantos litro deseja abastecer: '))
    valor_gas = litros * gasolina
    if litros <= 20:
        desco = valor_gas - (valor_gas * 0.04)
    else:
        desco = valor_gas - (valor_gas * 0.06)
    print(f'Você abasteceu com Gasolina e colocou {litros:.2f}l\n'
          f'O valor sem desconto é R${valor_gas:.2f}\n'
          f'Mas na promoção você vai pagar R${desco:.2f}')
else:
    print('Opção invalida tente novamente!')

