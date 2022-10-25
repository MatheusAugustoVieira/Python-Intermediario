from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: \033[1;33mMIRIM\033[m')
elif idade <= 14:
    print('Classificação: \033[1;32mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação: \033[1;34mJUNIOR\033[m')
elif idade <= 25:
    print('Classificação: \033[1;35mSÊNIOR\033[m')
elif idade > 25:
    print('Classificação: \033[1;31mMASTER\033[m')


