notas = []
i = 1
soma = 0
while i <= 4 :
    n = float (input ('Digite a nota: '))
    notas.append (n)
    soma += n
    i += 1
media = soma / (i-1)
print ('Notas: ', notas)
print ('Média: ', media)
