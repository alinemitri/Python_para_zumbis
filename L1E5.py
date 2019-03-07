valor_mercadoria = float (input ('Digite o valor da mercadoria: '))
desconto  = float (input ('Digite o valor do desconto (%): '))

v_desconto = valor_mercadoria*desconto/100
v_final = valor_mercadoria - v_desconto

print ('Valor do desconto: R$', v_desconto)
print ('Valor final: R$', v_final)
