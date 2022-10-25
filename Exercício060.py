'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

n = int(input('Digite um número para calcular seu Fatorial: '))
c = 0
f = 1
print('Calculando {}! ='.format(n), end='')
for c in range(0, n + 1):
    if c > 0:
        print('{}'.format(c), end='')
        print(' x ' if c > 1 else ' = ', end='')
    f *= c
    n -= 1
print('Seu fatorial é {}.'.format(f))
