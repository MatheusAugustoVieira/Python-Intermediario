print('-' * 40)
print('{:^40}'.format(' LOJÃO DO BARATÃO '))
print('-' * 40)
totcompra = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    totcompra += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
         menor = preço
         barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${totcompra:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')


