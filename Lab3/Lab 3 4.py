for i in range(1,10+1):
    for j in range(1,10+1):
        if i==1 or i==10 or j==1 or j==10:
            print("*",end=" ")
        else: 
            print(" ",end=" ")
    print(" ")