minutos = int (input ('Minutos usados de telefone: '))
if minutos < 200 :
    conta = 0.20 * minutos
if 200 <= minutos <= 400 :
    conta = 0.18 * minutos
if minutos > 400 :
    conta = 0.15 * minutos
print ('Conta de telefone: R$', conta)
