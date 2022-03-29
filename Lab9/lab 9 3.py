import random
file = open('asterisk.txt','w')
for i in range(50): 
    for j in range(50):
        s = random.randint(0,50)
        s1 = str(s)
        file.write(s1 + '*')
    file.write('\n')
file.close()