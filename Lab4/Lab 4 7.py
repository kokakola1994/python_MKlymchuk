num = int(input())
s = 0
from math import sqrt
for i in range(2,num+1) : s += 1/i**2 
print(s + 1)
print(sqrt(6*s))