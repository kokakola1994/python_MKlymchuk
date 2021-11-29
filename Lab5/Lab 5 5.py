l = []
print('List l in range from 100 to 150: ', end='\n')
for i in range(100,151) : 
    l.append(i)
print(l)
print('List in range from 100 to 150 with deleted every five element: ',end='\n')
del l[5:50:5]
print(l)