peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('\033[1;32mPARABÉNS\033[m, você está na faixa de PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, \033[1;35mcuidado!\033[m')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, \033[1;31mmuito cuidado!\033[m')
