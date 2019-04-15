letras = [ ]
i = 1
while i <= 10 :
    letras.append (input ('Letra: '))
    i += 1
i = 0
cont = 0
while i <= 9 :
    if letras [i] not in 'aeiou' :
        cont += 1
    i += 1
print ('Foram lidos %d consoantes' %cont)
