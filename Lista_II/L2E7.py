area = float (input ('Área a ser pintada: '))
litros = area / 3
if litros % 18 == 0 :
    latas = litros / 18
else :
    latas = 1 + litros // 18
valor = latas * 80

print (f'''Quantidade de latas: {latas}
Valor total: R${valor:.2f}''')
