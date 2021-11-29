n=int(input())
m=int(input())
for i in range(n,m+1): print(i,end=" ")
if m>n: n=m 
for i in range(n,m-1,-1): print(i,end=" ")
print("\n ")