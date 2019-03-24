'''
    Comentários de várias linhas com três aspas
    Faça um programa que leia três números e mostre o maior deles
'''
a = int (input ('Primeiro número: '))
b = int (input( 'Segundo número: '))
c = int (input ('Terceiro número: '))

if a >= b and a >= c :
    print ('Primeiro: %d' %a)
if b >= c :
    print ('Segundo: %d' %b)
else :
    print ('Terceiro: %d' %c)
    
