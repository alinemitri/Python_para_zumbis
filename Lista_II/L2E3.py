mp = float (input ('Massa de peixes (kg): '))
if mp < 50 :
    print ('Excesso = 0 \nMulta = 0')
else :
    excesso = mp - 50
    multa = excesso*4
    print ('Excesso = %.2f \nMulta = %.2f' %(excesso, multa))
