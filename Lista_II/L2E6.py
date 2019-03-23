salario = float (input( 'Salário / hora: '))
horas = float (input ('Horas trabalhadas no mês: '))

bruto = salario * horas
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato

'''
print ('a. + Salário Bruto: R$', bruto)
print ('b. - IR (11%): R$', ir)
print ('c. - INSS (8%): R$', inss)
print ('d. - Sindicato (5%): R$', sindicato)
print ('e. = Salário Líquido: R$', liquido)

'''

print (f'''a. + Salário Bruto: R${bruto:.2f}
b. - IR (11%): R${ir:.2f}
c. - INSS (8%): R${inss:.2f}
d. - Sindicato (5%): R${sindicato:.2f}
e. = Salário Líquido: R${liquido:.2f}''')

