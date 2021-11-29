def rect():
    for i in range(1,10+1):
        for j in range(1,10+1):
            if i==1 or i==10 or j==1 or j==10 or i==j:
                print("*",end=" ")
            else: 
                print(" ",end=" ")
        print(" ")

def rectdiag():
    for i in range(1,10+1):
        for j in range(1,10+1):
            if i==1 or i==10 or j==1 or j==10 or i==j or j==i or i+j==10+1:
                print("*",end=" ")
            else: 
                print(" ",end=" ")
        print(" ")


rect()
print("\n")
rectdiag()