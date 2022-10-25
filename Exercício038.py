n1 = int(input('PRIMEIRO número: '))
n2 = int(input('SEGUNDO número: '))
if n1 > n2:
    print('O \033[1;32mPRIMEIRO\033[m valor é maior')
elif n2 > n1:
    print('O \033[1;34mSEGUNDO\033[m valor é maior')
else:
    print(' Os dois valores são \033[1;35mIGUAIS\033[m')




