# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Faça um Programa que peça um número
e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
'''
print('=' * 40)
print('{:=^40}'.format(" PROGRAMA INTEIRO OU DECIMAL "))
print('=' * 40, '\n')


num = float(input('Numero original: '))

if num == round(num):
    print("Inteiro")
else:
    print("Decimal")
    print("Arredondado pra baixo: ", round(num-0.5) )
    print("Arredondado pra cima : ", round(num+0.5) )


