'''for n in range(1, 501):
    print(n, end=' ')'''

'''for n in range(1, 501, 2):
    print(n, end=' ')'''

'''for n in range(1, 501, 2):
    if n % 3 == 0:
        print(n, end=' ')'''

'''soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
print('A soma de todos os valores solicitados é {}'.format(soma))'''

'''soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1
        soma = soma + n
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))'''

soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1
        soma += n
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
