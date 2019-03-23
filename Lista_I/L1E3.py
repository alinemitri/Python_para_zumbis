d = int(input ('Digite o número de dias: '))
h = int (input ('Digite o número de horas: '))
m = int (input ('Digite o número de minutos: '))
s = int (input ('Digite o número de segundos: '))

total = d*24*3600 + h*3600 + m*60 + s
print ("O valor em segundos é %d" %total)
