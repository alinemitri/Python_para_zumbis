a = float ( input ('Digite o valor do lado 1: '))
b = float (input ('Digite o valor do lado 2: '))
c = float (input ('Digite o valor do lado 3: '))

check_a = a > abs (b - c) and a < b +c
check_b = b > abs (a - c) and b < a + c
check_c = c > abs (a - b) and c < a + b

if check_a == False or check_b == False or check_c == False :
    print ('Os lados não formam um triângulo')
elif a == b and a == c :
    print ('O triângo existe e é equilátero')
elif a == b or a == c or b == c :
    print ('O triângulo existe e é isósceles')
else :
    print ('O triângulo existe e é escaleno')

    
