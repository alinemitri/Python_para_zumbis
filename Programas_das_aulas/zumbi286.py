data = input ('Data de nascimento: ')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Outubro', 'Novembro', 'Dezembro']
info = data.split ('/')
mes = info [1]
print ('%s de %s de %s' %(info[0], meses [int(mes)-1], info [2]))
