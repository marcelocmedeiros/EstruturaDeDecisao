# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Faça um Programa que leia 2 números e em seguida
pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''
print('=' * 43)
print('{:=^40}'.format(" PROGRAMA QUAL OPERAÇÃO ELE DESEJA REALIZAR "))
print('=' * 43, '\n')


# variável 2 números
num_1 = float(input('Digite o 1° número: '))
num_2 = float(input('Digite o 2° número: '))
print('='*35)
# escolha da operação que deseja realizar
operacao = float(input('1 - par ou ímpar\n'
                       '2 - positivo ou negativo\n'
                       '3 - inteiro ou decimal\n'
                       'Qual das operações acima deseja realizar: '))
print('='*55)
#se par ou impar
if operacao == 1:
    print('Você escolheu saber se os números são PARES OU IMPARES.\n')
    if num_1 % 2 == 0:
        print(f'O número {int(num_1)} é PAR')
    else:
        print(f'O número "{int(num_1)}" é IMPAR')
    if num_2 % 2 == 0:
        print(f'O número "{int(num_2)}" é PAR')
    else:
        print(f'O número "{int(num_2)}" é IMPAR')
elif operacao == 2:
    print('Você escolheu saber se os números são POSITIVO OU NEGATIVO.\n')
    if num_1 < 0:
        print(f'O número "{int(num_1)}" é NEGATIVO')
    elif num_1 > 0:
        print(f'O número "{int(num_1)}" é POSITIVO')
    else:
        print(f'O número "{int(num_1)}" não é POSITIVO nem NEGATIVO, pois zero neutro')
    if num_2 < 0:
        print(f'O número "{int(num_2)}" é NEGATIVO')
    elif num_2 > 0:
        print(f'O número "{int(num_2)}" é POSITIVO')
    else:
        print(f'O número "{int(num_2)}" não é POSITIVO nem NEGATIVO, pois zero neutro')
elif operacao == 3:
    print('Você escolheu saber se os números são INTEIRO OU DECIMAL.\n')
    if num_1 == round(num_1):
        print(f'O número "{int(num_1)}" é INTEIRO')
    else:
        print(f'O número "{int(num_1)}" é DECIMAL')
    if num_2 == round(num_2):
        print(f'O número "{int(num_2)}" é INTEIRO')
    else:
        print(f'O número "{int(num_2)}" é DECIMAL')
else:
    print('Você digitou uma opção INVALIDA! Tente novamente.')



