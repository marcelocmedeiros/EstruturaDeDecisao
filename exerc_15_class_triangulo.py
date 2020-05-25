# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

print('='*48)
print('{:=^40}'.format(" PROGRAMA CATEGORIA DOS TRIÂNGULO "))
print('='*48, '\n')

# variável três segmentos para formar um triângulo
seg_1 = float(input('Qual o valor do 1° segmento: '))
seg_2 = float(input('Qual o valor do 2° segmento: '))
seg_3 = float(input('Qual o valor do 3° segmento: '))
print('='*45)
# condição para ser um triângulo
print('='*45)
if seg_1 < seg_2 + seg_3 and seg_2 < seg_1 + seg_3 and seg_3 < seg_1 + seg_2:
    print(f'Os segmentos {seg_1:.0f}, {seg_2:.0f} e {seg_3:.0f}\n'
          f'Formam um triângulo.')
    # condição para classificar o triângulo
    if seg_1 == seg_2 == seg_3:
        print('Este é um triãngulo classificado como Equilátero')
    elif seg_1 != seg_2 != seg_3:
        print('Este é um triãngulo classificado como Escaleno')
    else:
        print('Este é um triãngulo classificado como Isósceles')
else:
    print(f'Os segmentos {seg_1:.0f}, {seg_2:.0f} e {seg_3:.0f}\n'
          f'Não formam um triângulo.')
print('='*45)