# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''
print('=' * 53)
print('{:=^40}'.format(" PROGRAMA SOBRE A PARTICIPAÇÃO DA PESSOA NO CRIME "))
print('=' * 53, '\n')

# variável
print('Houve um assassinato e precisso fazer algumas peguntas\n'
      'Basta responder (0 para NAO - 1 para SIM).\n')
perg_1 = int(input('Telefonou para a vítima? '))
perg_2 = int(input('Esteve no local do crime? '))
perg_3 = int(input('Mora perto da vítima? '))
perg_4 = int(input('Devia para a vítima? '))
perg_5 = int(input('Já trabalhou com a vítima? '))
print('='*35)
# contando as respostas positivas
soma = perg_1 + perg_2 + perg_3 + perg_4 + perg_5

# classificação sobre a participação da pessoa no crime
if soma <= 1:
    print('Diante das sua respostas posso afirma que...\n'
          'VOCÊ É INOCENTE!')
elif soma == 2:
    print('Não sai da cidade sem cominucar a Polícia.\n'
          'VOCÊ É SUSPEITO!')
elif soma >= 3 and soma <= 4:
    print('Você está preso...\n'
          'VOCÊ É CÚMPLICE DESTE CRIME!')
elif soma == 5:
    print('Conforme suas respostas já encontrei o culpado...\n'
          'VOCÊ É O ASSASSINO!')



