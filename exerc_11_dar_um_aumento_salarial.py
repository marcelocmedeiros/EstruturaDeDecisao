# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 18/03/2020

'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador
e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

print('='*55)
print('PROGRAMA PARA AUMENTO DE SALÁRIO DOS COLABORADORES')
print('='*55,'\n')

# variáveis valor do salário
salario = float(input('Qual o valor do seu salário:R$ '))
print('='*40,'\n')
# condições de reajuste salarial
if salario <= 280:
    reajuste = 20
    aumento = salario * (reajuste/ 100)
    novo = salario + aumento
elif salario > 280 and salario <= 700:
    reajuste = 15
    aumento = salario * (reajuste / 100)
    novo = salario + aumento
elif salario > 700 and salario <= 1500:
    reajuste = 10
    aumento = salario * (reajuste / 100)
    novo = salario + aumento
else:
    reajuste = 5
    aumento = salario * (reajuste / 100)
    novo = salario + aumento
print(f'O seu salário antes do reajuste era R${salario}.\n'
      f'O seu percentual de aumento aplicado foi {reajuste}%.\n'
      f'O valor do aumento salarial R${aumento:.2f}.\n'
      f'O novo salário, após o aumento será R${novo:.2f}.',)
