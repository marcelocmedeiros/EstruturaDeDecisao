# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 18/03/2020

'''
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

print('='*35)
print('PROGRAMA PARA FOLHA DE PAGAMENTO')
print('='*35,'\n')

# variáveis valor da sua hora e a quantidade de horas trabalhadas no mês
valor_hora = float(input('Qual o valor da sua hora de trabalho:R$ '))
num_horas = int(input('Qual a quantidade de horas trabalhadas no mês: '))
print('='*40,'\n')
# valor do salário
salario = valor_hora * num_horas
# valor do desconto do inss
inss = 10
inss_valor = salario * (inss/100)
# valor do fgts
fgts = 11
fgts_valor = salario * (fgts/100)

# condições para o desconto do IR
# até 900 (inclusive) - isento
if salario <= 900:
    ir = 0
    ir_valor = salario * (ir / 100)
# até 1500 (inclusive) - desconto de 5%
elif salario > 900 and salario <= 1500:
    ir = 5
    ir_valor = salario * (ir / 100)
# até 2500 (inclusive) - desconto de 10%
elif salario > 1500 and salario <= 2500:
    ir = 10
    ir_valor = salario * (ir / 100)
# acima de 2500 - desconto de 20%
else:
    ir = 20
    ir_valor = salario * (ir / 100)
# total dos descontos obrigaórios
total_desc = ir_valor + inss_valor
# valor do salário liquido
salario_liq = salario - (ir_valor + inss_valor)

print(f'O seu Salário Bruto ({valor_hora:.0f} * {num_horas}) R${salario:.2f}.\n'
      f'O seu desconto do IR (-{ir})  foi R${ir_valor:.2f}%.\n'
      f'O seu desconto do INSS (-{inss})  foi R${inss_valor:.2f}.\n'
      f'O valor do FGTS ({fgts})  foi R${fgts_valor:.2f}.\n'
      f'O Total de descontos R${total_desc:.2f}.\n'
      f'O valor do salário liquido R${salario_liq:.2f}',)
