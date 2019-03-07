cigarro = int (input ('Cigarros por dia: '))
ano = int (input ('Quantos anos já fumou: '))
n = cigarro*ano*365
perda = n*10/(60*24)
print ('O fumante perderá %.2f dias de vida' %perda)
