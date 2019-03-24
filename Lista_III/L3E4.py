f1 = 1
f2 = 1
i = 2
n = int (input ('Digite n: '))
while i < n :
    fi = f1 + f2
    f1 = f2
    f2 = fi
    i = i + 1
print ('F(%d) = %d' %(i, fi))
