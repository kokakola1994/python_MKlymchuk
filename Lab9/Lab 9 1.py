import random
file = open('liczby','w')
for i in range(0,20): 
    s = random.randint(1,100)
    s1 = str(s)
    file.write(s1 + ' ')
file.close()