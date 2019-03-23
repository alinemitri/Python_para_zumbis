ano = int( input ('Digite o ano: '))
if ano % 4 != 0 :
    print ('O ano %d não é bissexto!' %ano)
elif ano % 100 != 0 :
    print ('O ano %d é bissexto!' %ano)
elif ano % 400 != 0 :
    print ('O ano %d não é bissexto!' %ano)
else :
    print ('O ano %d é bissexto!' %ano)
