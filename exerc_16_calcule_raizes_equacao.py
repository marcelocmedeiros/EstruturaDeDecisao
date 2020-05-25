# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c
e fazer as consistências, informando ao usuário nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
    e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais.
        Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
        informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais;
        informe-as ao usuário;
'''

print('='*50)
print('{:=^40}'.format(" PROGRAMA QUE CALCULE AS RAÍZES DA EQUAÇÃO 2° GRAU "))
print('='*50, '\n')

print('EQUAÇÃO: ax² + bx + c')
# variável ax² + bx + c, informar as variéis: a, b, c
a = int(input('Dentro da equação acima informe a variável "a": '))
# condição caso "a" seja == 0
if a == 0:
    print('Programa encerrado!!!\n'
          'Valor não satisfaz a condição para ser uma equação do 2° grau')
# "a" != 0
else:
    b = int(input('Dentro da equação acima informe a variável "b": '))
    c = int(input('Dentro da equação acima informe a variável "c": '))
    delta = b ** 2 - 4 * a * c
    # delta calculado for negativo
    if delta < 0:
        print('\n', 'Programa encerrado!!!\n'
              f'Valor de delta é negativo {delta}\n'
              f' portanto a equação não possui raizes reais')
    elif delta == 0:
        x = (-b) / (2 * a)
        print('\n', 'Valor de delta é igual a "0"\n'
              f'Portanto a equação possui apenas uma raiz real que é {x}')
    else:
        x_1 = ((-b) + delta) / (2 * a)
        x_2 = ((-b) - delta) / (2 * a)
        print('\n', 'Valor de delta é positivo\n'
              f'Portanto a equação possui duas raiz reais que são {x_1:.2f} e {x_2:.2f}')




