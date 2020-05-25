# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

print('='*48)
print('{:=^40}'.format(" PROGRAMA EXIBA O DIA CORRESPONDENTE DA SEMANA "))
print('='*48, '\n')

# variáveis digitar números (1-7)
num = int(input('Digite um número entre 1 e 7: '))
# relacionando o número e o dia da semana
if num == 1:
    print('DOMINGO')
elif num == 2:
    print('SEGUNDA')
elif num == 3:
    print('TERÇA')
elif num == 4:
    print('QUARTA')
elif num == 5:
    print('QUINTA')
elif num == 6:
    print('SEXTA')
elif num == 7:
    print('SÁBADO')
else:
    print('VALOR INVÁLIDO!!!')