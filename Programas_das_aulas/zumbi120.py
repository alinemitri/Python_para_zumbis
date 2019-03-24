minutos = int (input ('Minutos usados de telefone: '))
if minutos < 200 :
    preço = 0.20
else :
    if minutos <= 400 :
        preço = 0.18
    else :
        if minutos > 800 :
            preço = 0.08
        else :
            preço = 0.15
print ('Conta de telefone: R$%6.2f' %(minutos*preço))
