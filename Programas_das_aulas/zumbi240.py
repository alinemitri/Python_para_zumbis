n = 1
soma = 0
media = 0
while n <= 10 :
    x = int (input ('Digite o %d número: ' %n))
    soma = soma + x
    n = n + 1
media = soma / (n-1)
print ('Média: %f' %media)
