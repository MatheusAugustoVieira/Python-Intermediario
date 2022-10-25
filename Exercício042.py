print('\033[1;32m-=-\033[m'*9)
print('\033[1;34mAnalisador de Triângulos\033[m')
print('\033[1;32m-=-\033[m'*9)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m um triângulo!', end='')
    if r1 == r2 == r3:
        print('\033[1;35mEQUILÁTERO!\033[m')
    elif r1 != r2 != r3 != r1:
            print('\033[1;34mESCALENO\033[m')
    else:
        print('\033[1;36mISÓSCELES\033[m')
else:
    print('Os segmentos acima \033[1;31mNÃO PODEM FORMAR\033[m um triângulo!')
