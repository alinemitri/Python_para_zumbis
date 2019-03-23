s = float (input ('Digite o valor do salário atual: '))
a = float (input ('Digite o valor do aumento (%): '))

s_a = (a/100 + 1)*s
valor_a = s_a - s

print ('O salário aumenta para R$%.2f e o aumento é de R$%.2f' %(s_a, valor_a))

