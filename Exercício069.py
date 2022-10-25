'''pessoa = str
while True:
    pessoa1 = print(str('Quer Continuar? [S/N]')).strip().upper()[0]
    if pessoa1 == 'S':
        print('-' * 20)
        print('CADASTRE UMA PESSOA')
        print('-' * 20)
        id = int(input('idade: '))
        se = str(input('Sexo: [M/F] '))
    elif pessoa1 == 'N':
        break
print('Obrigado pelo seu cadastro')'''

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            totH += 1
        if sexo == 'F' and idade < 20:
            totM20 += 1
        resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
