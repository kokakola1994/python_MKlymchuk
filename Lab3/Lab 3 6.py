for i in range(1,11+1):
    for j in range(1,11+1):
        if i==1 or i==11 or j==1 or j==11 or i%2==1 or j%2==1:
            print("*",end=" ")
        else: 
            print(" ",end=" ")
    print(" ")