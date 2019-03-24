A = 80000
cresc_A = 0.03
B = 200000
cresc_B = 0.015
ano = 0
while A < B :
    A = A * (1 + cresc_A)
    B = B * (1 + cresc_B)
    ano = ano + 1
print ('Serão necessários %d anos para A ultrapassar ou igualar B' %ano)
