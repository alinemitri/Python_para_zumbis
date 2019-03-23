n1 = float (input ('Digite o primeiro valor: '))
n2 = float (input ('Digite o segundo valor: '))
n3 = float (input ('Digite o terceiro valor: '))

if n1 > n2 and n1 > n3 :
    maior = n1
elif n2 > n3 :
    maior = n2 
else :
    maior = n3

if n1 < n2 and n1 < n3 :
    menor = n1
elif n2 < n3 :
    menor = n2
else :
    menor = n3

print ('O maior valor é ', maior)
print ('O menor valor é ', menor)
