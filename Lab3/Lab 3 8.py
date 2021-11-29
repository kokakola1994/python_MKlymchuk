def rect():
    for i in range(1,10+1):
        for j in range(1,10+1):
            if i==1 or i==10 or j==1 or j==10 or i<6 and j-1<i or j>5 and i>j or i>6 and i>j+4 or j>5 and i<6 and j%5<i:
                print("*",end=" ")
            else: 
                print(" ",end=" ")
        print(" ")

rect()