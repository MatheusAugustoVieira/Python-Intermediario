'''n = s = 0
while True:
    n1 = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    soma = 1 * n1
    soma2 = 2 * n1
    soma3 = 3 * n1
    soma4 = 4 * n1
    soma5 = 5 * n1
    soma6 = 6 * n1
    soma7 = 7 * n1
    soma8 = 8 * n1
    soma9 = 9 * n1
    soma10 = 10 * n1
    print(f'{n1} x 1 = {soma}')
    print(f'{n1} x 2 = {soma2}')
    print(f'{n1} x 3 = {soma3}')
    print(f'{n1} x 4 = {soma4}')
    print(f'{n1} x 5 = {soma5}')
    print(f'{n1} x 6 = {soma6}')
    print(f'{n1} x 7 = {soma7}')
    print(f'{n1} x 8 = {soma8}')
    print(f'{n1} x 9 = {soma9}')
    print(f'{n1} x 10 = {soma10}')
    if n1 <= 0:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')'''

while True:
    print('\033[1;31mDigite um número negativo para encerrar\033[m')
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
