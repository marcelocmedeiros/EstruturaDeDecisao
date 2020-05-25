# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
print('=' * 40)
print('{:=^40}'.format(" PROGRAMA CLASSES MÉDIA COM INFORMAÇÃO "))
print('=' * 40, '\n')

# variável três notas
nota_1 = float(input('Escreva 1° nota: '))
nota_2 = float(input('Escreva 2° nota: '))
nota_3 = float(input('Escreva 3° nota: '))
print('=' * 45)
# calculo média
media = (nota_1 + nota_2 + nota_3) / 3
# analise da média e a sua mensagem
if media == 10:
    condi = 'APROVADO COM DISTINÇÃO'
elif media >= 7 and media < 10:
    condi = 'APROVADO'
elif media < 7:
    condi = 'REPROVADO'

print(f'Sua notas foram: {nota_1:.2f}, {nota_2:.2f} e {nota_3:.2f}.\n'
      f'Sua média alcançada foi de {media:.2f}.\n'
      f'Portanto você está {condi}')
