print('\033[1;36mTABUADA V.2.0\033[m')
num = int(input('Digite um número para ver sua tabuada: '))
print('\033[1;34m=\033[m'*12)
for t in range(1, 11):
    print('\033[1;32m{} x {:2} = {}\033[m'.format(num, t, num*t))
print('\033[1;34m=\033[m'*12)
