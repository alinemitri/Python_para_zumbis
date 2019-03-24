a = int (input ("Digite o primeiro número inteiro positivo: "))
b = int (input ("Digite o segundo número inteiro positivo: "))
if a > b :
    maior = a
    menor = b
else :
    maior = b
    menor = a
resto = maior % menor
while resto != 0 :
    maior = menor
    menor = resto
    resto = maior % menor
print ("mdc (%d, %d) : %d" %(a, b, menor))
