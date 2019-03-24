n = int (input ('Digite o valor de n: '))
i = 1
fat = 1
while i <= n :
    fat = fat * i
    i = i + 1
print ('Fatorial de %d: %d' %(n, fat))
