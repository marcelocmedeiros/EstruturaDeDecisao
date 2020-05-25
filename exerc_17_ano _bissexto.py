# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 18/03/2020

'''
Faça um Programa que peça um número correspondente a um determinado ano
e em seguida informe se este ano é ou não bissexto.
'''
print('=' * 40)
print('{:=^40}'.format(" PROGRAMA ANO BISSEXTO "))
print('=' * 40, '\n')

# importando a função date que mostra o ano atual do PC
from datetime import date

# variável  ano
ano = int(input('Quer saber se o ano é ou não BISSEXTO, digite o ano: '))
print('='*25)
if ano == 0:
    ano  = date.today().year
# condição para o ano ser bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Você edigitou o ano {ano}.\n'
          f'Este ano é BISSEXTO!!! ')
else:
    print(f'Você edigitou o ano {ano}.\n'
          f'Este ano NÃO É BISSEXTO!!! ')
print('='*25)
