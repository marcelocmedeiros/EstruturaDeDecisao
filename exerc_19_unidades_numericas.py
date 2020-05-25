# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 20/03/2020

'''
Faça um Programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
print('=' * 40)
print('{:=^40}'.format(" PROGRAMA CLASSES NÚMERICAS "))
print('=' * 40, '\n')

# variável um número inteiro < 1000
num = int(input('Escreva um número qualquer entre 0 a 9999: '))
print('=' * 45)
# calculo num // (u=1; d=10; c=100; m=1000), (retonar o quociente)
# que  % 10 (me mostra o resto) que será acorrespondente {u; d; c}
if num> 0 and num < 1000:
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    print('Analisando seu número...\n')
    print(f'O número digitado foi "{num}"\n'
          f'Ele tem "{c}" centenas, "{d}" dezenas e "{u}" unidades.')
else:
    print("Insira um numero maior que zero (0) ou menor que (1000)")