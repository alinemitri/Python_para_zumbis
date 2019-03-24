velocidade = int (input ('Velocidade do carro: '))
if velocidade <= 110 :
    print ('Velocidade abaixo do limite')
else :
    multa = (velocidade - 110)*5
    print ('Velocidade acima do limite! Multa: R$', multa)
