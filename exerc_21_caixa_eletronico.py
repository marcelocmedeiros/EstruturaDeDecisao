# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque
e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais,
        o programa fornece duas notas de 100,
         uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais,
        o programa fornece três notas de 100,
        uma nota de 50, quatro notas de 10,
        uma nota de 5 e quatro notas de 1.
'''
print('=' * 40)
print('{:=^40}'.format(" PROGRAMA PARA UM CAIXA ELETRÔNICO "))
print('=' * 40, '\n')

# variável saque
saque = int(input('Nesse caixa só pode ser sacado valores entre R$ 10 e R$ 600\n'
                  'Quanto você quer sacar?:R$ '))

print('=' * 45)
# calculo fatiando o valor do saque
# num // (u=1; d=10; c=100; m=1000), (retonar o quociente)
# que  % 10 (me mostra o resto) que será acorrespondente {u; d; c}
if saque >= 10 and saque <= 600:
    u = saque // 1 % 10
    d = saque // 10 % 10
    c = saque // 100 % 10

    print(f'O valor sacado foi R${saque:.2f}\n'
          f'Portanto você reberá "{c}" notas de cem reais')
    if d < 5:
        print(f'"{d}" notas de dez reais')
    elif d >= 5:
        un = d - 5
        d = 1
        print(f'"{d}" notas de cinquenta reais, {un} notas de dez reais')
    elif d == 5:
        d = 1
        print(f'"{d}" notas de cinquenta reais')
    if u < 5:
        print(f'"{u}" notas de um real')
    elif u >= 5:
        un = u - 5
        u = 1
        print(f'"{u}" notas de cinco reais, {un} notas de um reais')
    elif u == 5:
        u = 1
        print(f'"{u}" notas de cinco reais')
else:
    print("Valor incorreto digite novamente!)")