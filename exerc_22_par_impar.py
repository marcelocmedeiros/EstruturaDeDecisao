# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Faça um Programa que peça um número inteiro
e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
'''
print('=' * 40)
print('{:=^40}'.format(" PROGRAMA PAR OU IMPAR "))
print('=' * 40, '\n')

# variável número inteiro
num = int(input('Digite um número inteiro: '))
print('='*35)
# condição para ser par % 2 == 0
if num % 2 == 0:
    print('Você digitou um número PAR')
else:
    print('Você digitou um número IMPAR')
