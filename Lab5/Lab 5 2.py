l = []
for i in range(1,11) :
    if i**2%2 == 0 :
       l.append(-i**2)
    else :
        l.append(i**2)
print(l)