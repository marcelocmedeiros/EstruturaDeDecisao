# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Faça um programa que lê as duas notas parciais obtidas por um aluno
numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média,
o conceito correspondente e a mensagem “APROVADO”
se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

print('='*48)
print('{:=^40}'.format(" PROGRAMA MÉDIA COM ATRIBUIÇÃO DE CONCEITOS "))
print('='*48, '\n')

# variáveis recebe duas notas
nota_1 = float(input('Digite 1° nota: '))
nota_2 = float(input('Digite 2° nota: '))
# variável média
media = (nota_1 + nota_2) / 2
print(f'Sua 1° nota foi {nota_1:.2f} e a seugunda foi {nota_2:.2f}.\n'
      f'Com isso sua média será {media:.2f}.')

# relacionando média com os conceitos
if 0 <= media < 4:
    conc = "E"
    print(f'Assim você obteve o conceito {conc}\n'
          f'Infelimente você está REPROVADO!')
elif 4 <= media < 6:
    conc = "D"
    print(f'Assim você obteve o conceito {conc}\n'
          f'Infelimente você está REPROVADO!')
elif 6 <= media < 7.5:
    conc = "C"
    print(f'Assim você obteve o conceito {conc}\n'
          f'Parabéns você está APROVADO!')
elif 7.5 <= media < 9:
    conc = "B"
    print(f'Assim você obteve o conceito {conc}\n'
          f'Parabéns você está APROVADO!')
elif 9 <= media < 10:
    conc = "A"
    print(f'Assim você obteve o conceito {conc}\n'
          f'Parabéns você está APROVADO!')
else:
    print('VALORES INVÁLIDOS!!!')
